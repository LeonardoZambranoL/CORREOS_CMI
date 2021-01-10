# -*- coding: utf-8 -*-
"""
Correos automáticos,
Diseñado para correos personalizables
Leonardo :D

"""




import smtplib
from email.message import EmailMessage
import time
from string import Template
from tkinter import *
import mimetypes

def register_func(Template):
    #creando un nombre para guardar registro
    
    Fecha = time.strftime("%d-%m-%Y %H-%M-%S")

    return "./Register/"+Template+"/"+Template+" "+Fecha+".txt"

def lectura_de_datos(Template_name):

    dir_Template="./info/Templates/"+Template_name+"/"

    # segun las pruebas que hice con el código, encoding="utf8" da problemas si la plantilla se creó desde el menú "PLANTILLA NUEVA - CMI"
    # pero si la plantilla se intruduce manualmente como un .txt, la falta de encoding="utf8" causa errores
    # para cubrir todos los casos y evitar posibles errores, la siguiente sintaxis
    
    try:
        with open(dir_Template+"PLAIN.txt","r",encoding="utf8") as info:
            Template_contents_plain = Template(info.read())
    except:
        with open(dir_Template+"PLAIN.txt","r") as info:
            Template_contents_plain = Template(info.read())
        
    try:    
        with open(dir_Template+"HTML.txt","r",encoding="utf8") as info:
            Template_contents_html = Template(info.read())
    except:
        with open(dir_Template+"HTML.txt","r") as info:
            Template_contents_html = Template(info.read())
        
    Template_contents=(Template_contents_plain,Template_contents_html)

    return Template_contents


def send(app,smtp, Template_contents, Destinatarios, dir_Register, Template, Email,Subject,Attachments=[]):
    
    

    nombre = Destinatarios[1].title()
    correo = Destinatarios[2]
    correo = correo.replace(" ", "").strip()

    # PERSONALIZACIÓN
    # ACTIVA ESTO MÁS TARDE
    """
    codigo = Destinatarios[0]
    colegio= Destinatarios[3]
    P1=Destinatarios[5]
    P2=Destinatarios[6]
    P3=Destinatarios[7]
    P4=Destinatarios[8]
    Total=Destinatarios[9]
    Premio=Destinatarios[10]


    if Premio is None:
        Premio=""
    if Premio.lower()!="medalla":
        #print(Premio)
        Premio_plano="Gracias por participar en nuestra Olimpiada"
        Premio_html="Gracias por participar en nuestra Olimpiada"

    else:
        #print(Premio)
        Premio_html="Por tanto obtuviste una: <b>"+Premio+"</b><b>Felicitaciones!</b>"
        Premio_plano="Por tanto obtuviste una:   "+Premio+"    Felicitaciones!"

    """
    with open(dir_Register, "a") as registro:

        #print(correo + "\n" * 2)
        registro.write(correo + "\n" * 2)

        try:

            # crear mensaje
            msg = EmailMessage()
            msg["Subject"] = Subject
            msg["From"] = Email
            del msg["to"]
            msg["to"] = correo
            # mensaje plano
            # ,P1=P1,P2=P2,P3=P3,P4=P4,Total=Total,PREMIO=Premio_plano
            msg.set_content((Template_contents[0]).substitute(NAME=nombre))
            # mensaje html
            # ,P1=P1,P2=P2,P3=P3,P4=P4,Total=Total,PREMIO=Premio_plano
            msg.add_alternative((Template_contents[1]).substitute(NAME=nombre), subtype="html")
            app.update()
            # añadir attachments
            for att in Attachments:
                
                print("\t" + att)
                registro.write("\t" + att + "\n")
                with open(att, "rb") as attachment:
                    maintype, subtype = mimetypes.guess_type(attachment.name)[0].split("/")
                    print("\t" + "correcto")
                    registro.write("\t" + "correcto\n\n")
                    attachment_content = attachment.read()
                    msg.add_attachment(attachment_content, maintype=maintype, subtype=subtype,
                                       filename=att.split("/")[-1][0:-4])
                app.update()
                
            # envio de correo

            smtp.send_message(msg)

            app.update()
            
            # confirmacion de correo enviado
            registro.write("\t" + "enviado\n\n")
            with open("./Register/" + Template + "/YA ENVIADO.txt", "a") as enviado:
                enviado.write(correo + "\n")

            #print("\t" + "enviado")

        except Exception as e:

            # aviso correo fallido
            registro.write("\t" + "error\n\n")
            #print("\t" + "error" + "\n" * 2)
            registro.write(str(e)+"\n")
            #print("\t" + "no enviado" + "\n" * 2)
            app.update()
            with open("./Register/" + Template + "/NO ENVIADO.txt", "a") as no_enviado:
                no_enviado.write(correo + "\n")
            raise
            