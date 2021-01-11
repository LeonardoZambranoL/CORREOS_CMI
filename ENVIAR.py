import func
import MySQL_for_massive_mails
import requests
import smtplib
import time
from tkinter import *




def run(Greeting,Subject,Template_name,Attachments_base,Attachment_personalizado,Warnings,Progress_bar,app):

    ammount_sent=0
    Attachments_base=["./info/Atts/"+a for a in Attachments_base]

    try:
        Template_contents=func.lectura_de_datos(Template_name)
    except Exception as e:
        print("-----EL NOMBRE DE LA PLANTILLA NO ES VALIDO--------\n"+str(e))
        Warnings.config(text="-----EL NOMBRE DE LA PLANTILLA NO ES VALIDO--------\n"+str(e))
        app.update()
        return
    
    ammount_not_sent=MySQL_for_massive_mails.count_new(Greeting,Template_name)
    if type(ammount_not_sent)==str and "Error" in ammount_not_sent:
        print("-----PROBLEMAS CON LA BASE DE DATOS; ALGUNO DE LOS CAMPOS RELACIONADOS ES INCORRECTO O EL SERVIDOR NO ESTÁ ENCENDIDO--------\n"+ ammount_not_sent)
        Warnings.config(text="-----PROBLEMAS CON LA BASE DE DATOS; ALGUNO DE LOS CAMPOS RELACIONADOS ES INCORRECTO O EL SERVIDOR NO ESTÁ ENCENDIDO--------\n"+ ammount_not_sent)
        app.update()
        return
        
    Progress_bar.config(text=str(ammount_sent)+" de "+str(ammount_not_sent))
    
    
    
    #definiendo limites horarios --- EN CASO DE TENER MUCHOS CORREOS EN LA BASE DE DATOS; ESTO CONTROLA
    #QUE LA LISTA DE CORREOS SE RENUEVE CADA HORA O CUANDO SE VACIE; PARA NO TENER
    #MILES DE CORREOS EN MEMORIA AL MISMO TIEMPO
    hora_limite={}
    for a in range(0,23):
        hora_limite[a]=a+1
    hora_limite[23]=0
    
    del a
    
    
    def envio_masivo(limite_correos,delay,hora_de_inicio,ammount_sent):
        #estado
        
        
        print("---------ENVIANDO---------\n\n")
        Warnings.config(text="---------ENVIANDO---------")
        app.update()
        dir_Register=func.register_func(Template_name)
        
        #registrar correos ya enviados
        Destinatarios=MySQL_for_massive_mails.fetch_new_mails(Greeting,Template_name,limite_correos)
        #print(Destinatarios)
        #en caso de haber error de lectura, Destinatarios=Mensaje de error
        while type(Destinatarios)==str:
            print(Destinatarios,"\n\n")
            for number in range(50):
                app.after(100)
                app.update()
            Destinatarios=MySQL_for_massive_mails.fetch_new_mails(Greeting,Template_name,limite_correos)
        
        #Si continuar==True, se realiza otra ronda de envios, caso contrario se termina el programa
        continuar=True
        if Destinatarios==[]:
            continuar=False
        

        with smtplib.SMTP_SSL(Greeting[0],Greeting[1]) as smtp:
            #inicio de sesión

            smtp.login(Greeting[2],Greeting[3])
    
            while Destinatarios:
           
                #print(Destinatarios[0][0:3])
                hora=int(time.strftime("%H"))
                if hora==hora_limite[hora_de_inicio]:
                    #print("------------- HORA LIMITE ALCANZADA, REINICIANDO ENVIO -------------\n\n")
                    break

                try:
                    #print("EN TRY")
                    if Attachment_personalizado:
                        Attachments=[a+Destinatarios[0][0]+".pdf" for a in Attachments_base]
                    else:
                        Attachments=Attachments_base
                    
                    func.send(app,smtp,Template_contents,Destinatarios[0] ,dir_Register,Template_name,Greeting[2],Subject,Attachments)
                    app.update()
                    #Dest_df.ENVIO[Dest_df["Correo Electrónico"]==Destinatarios[0],["ENVIO"]]="YA"
                    
                    #resultados
                    
                    update=MySQL_for_massive_mails.update_status(Greeting,Template_name,"ENVIADO",Destinatarios[0][0])
                    print(update,"| ENVIADO |",Destinatarios[0][0],"\n")
                    Warnings.config(text=update+"  |  ENVIADO  |  "+Destinatarios[0][0])
                    app.update()
                    #print(Dest_df)
                    del Destinatarios[0]
                    
    
                    
                            #aviso correofallido
                except Exception as e:
                    app.update()
                    #raise
                    
                    #CHEQUEAR CONECCIÓN A INTERNET
                    try:
                        requests.get("http://www.google.com", timeout=5)
                    except:
                        #avisos
                        print("---HAY FALLOS CON SU CONECCIÓN DE INTERNET---\n\n")
                        Warnings.config("---HAY FALLOS CON SU CONECCIÓN DE INTERNET---")
                        app.update()
                        break
                    
                    #Dest_df.ENVIO[Dest_df["Correo Electrónico"]==Destinatarios[0]]="ERROR"
                    #resultados
                    update=MySQL_for_massive_mails.update_status(Greeting,Template_name,"ERROR",Destinatarios[0][0])
                    print(update,"|  ERROR  |",Destinatarios[0][0],"\n"+str(e))
                    Warnings.config(text=update+"  |   ERROR   |  "+Destinatarios[0][0]+"\n"+str(e))
                    ammount_sent += 1
                    Progress_bar.config(text=str(ammount_sent) + " de " + str(ammount_not_sent))
                    for number in range(100):
                        app.after(delay * 10)
                        app.update()
                    #print(Dest_df)
                    del Destinatarios[0]
                    break
                
                ammount_sent+=1
                Progress_bar.config(text=str(ammount_sent)+" de "+str(ammount_not_sent))        
                app.update()
                
                for number in range(100):
                    app.after(delay*10)
                    app.update()
                
        
        
        
        
        return continuar, ammount_sent
    
    
    
    while True:
        #ENVIA LA HORA DE INICIO; DESPUES DE UNA HORA EL CÓDIGO
        #SE ROMPE Y RENUEVA LA LISTA DE CORREOS EN MEMORIA
        
        hora_de_inicio=int(time.strftime("%H"))
        
            
        try:
            #el delay es útil para evitar rebasar el límite de correos diarios (función envio_masivo, segundo parámetro)
            #en caso de tener una base de datos de gran tamaño, el delay puede ser usado para controlar la cantidad
            #de correo enviados cada hora 
            #esta función la saque de un proyecto que trabajé en paralelo a este (enfocado en tener un servidor encendido 24 horas al dia
            # enviando correos) pero decidí mantenerla aqui pues podría resultar util
            
            #dudo que sea el caso, por tanto el delay que puse es de 2 segundos, pero usted puede cambiarlo
            continuar, ammount_sent=envio_masivo(200,2,hora_de_inicio,ammount_sent)
            if not continuar:
                #print("\n\n-------------YA NO HAY MAS CORREOS!!!!!!!!!!!!!!!!-------------")
                break
        except Exception as e:

            print("------------ERROR: ALGUNO DE LOS CAMPOS RELACIONADOS AL CORREO ES INCORRECTO------------\n"+str(e))
            Warnings.config(text="------------ERROR: ALGUNO DE LOS CAMPOS RELACIONADOS AL CORREO ES INCORRECTO------------\n"+str(e))
            for number in range(100):
                app.after(100)
                app.update()
      
        
    #estado
    print("\n\n-------------FIN!!!!!!!!!!!!!!!!-------------")
    Warnings.config(text="---------FIN---------")
    app.update()
    return
