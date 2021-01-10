# -*- coding: utf-8 -*-
#GUI
from tkinter import *
from tkinter import filedialog
#archivos
import os
import os.path 
import shutil
#enciptar
from cryptography.fernet import Fernet
#otros .py
import WINDOW_OPENER
import  ENVIAR
#extras
import webbrowser

def modifier(func_1):
    modificar = Toplevel()

    modificar.title("MODIFICAR DATOS - CMI")
    modificar.geometry("500x500")
    modificar.iconbitmap("./icons/WERKZEUG.ico")

    #modificar.bind("<Escape>", lambda event: modificar.attributes("-fullscreen",not modificar.attributes("-fullscreen")))
    modificar.resizable(0,0)#######§
    
    #Definir Frames""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""
    Frame_Correo=LabelFrame(modificar, text="",pady=10)
    Frame_Texto_Correo=LabelFrame(modificar, text="",pady=30)
    Frame_Entry_Correo=LabelFrame(modificar, text="",pady=34)
    """"""""""""""""""
    Frame_DATA_BASE=LabelFrame(modificar, text="",pady=10)
    Frame_Texto_DATA_BASE=LabelFrame(modificar, text="",pady=30)
    Frame_Entry_DATA_BASE=LabelFrame(modificar, text="",pady=35)
    
    #Colocar Frames""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""
    Frame_Correo.grid(row=1,column=0,columnspan=2,sticky=W+E)
    Frame_Texto_Correo.grid(row=2,column=0,sticky=W+E)
    Frame_Entry_Correo.grid(row=2,column=1,sticky=W+E)
    """"""""""""""""""
    Frame_DATA_BASE.grid(row=3,column=0,columnspan=2,sticky=W+E)
    Frame_Texto_DATA_BASE.grid(row=4,column=0,sticky=W+E)
    Frame_Entry_DATA_BASE.grid(row=4,column=1,sticky=W+E)
    """"""""""""""""""    
    
    #Definir Widgets""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    vacio=Label(modificar,text="")
    
    """"""""""""""""""
    Titulo_Correo=Label(Frame_Correo,text="INFORMACIÓN SOBRE CORREO")
    
    Texto_SMTP=Label(Frame_Texto_Correo,text="DIRECCIÓN SMTP")
    Texto_PUERTO=Label(Frame_Texto_Correo,text="PUERTO")
    Texto_DIRECCIÓN=Label(Frame_Texto_Correo,text="DIRECCIÓN DE CORREO")
    Texto_PASSWORD=Label(Frame_Texto_Correo,text="CONTRASEÑA")
    
    Entry_SMTP= Entry(Frame_Entry_Correo)
    Entry_PUERTO=Entry(Frame_Entry_Correo)
    Entry_DIRECCIÓN= Entry(Frame_Entry_Correo)
    Entry_PASSWORD=Entry(Frame_Entry_Correo)


    """"""""""""""""""

    Titulo_DATA_BASE=Label(Frame_DATA_BASE,text="INFORMACIÓN SOBRE BASE DE DATOS")
    
    Texto_HOST=Label(Frame_Texto_DATA_BASE,text="HOST")
    Texto_USER=Label(Frame_Texto_DATA_BASE,text="USER")
    Texto_DATA_BASE_PASSWORD=Label(Frame_Texto_DATA_BASE,text="CONTRASEÑA")
    Texto_Db=Label(Frame_Texto_DATA_BASE,text="NOMBRE DE LA BASE DE DATOS")
    Texto_Table=Label(Frame_Texto_DATA_BASE,text="NOMBRE DE LA TABLA")

    Entry_HOST= Entry(Frame_Entry_DATA_BASE)
    Entry_USER= Entry(Frame_Entry_DATA_BASE)
    Entry_DATA_BASE_PASSWORD=Entry(Frame_Entry_DATA_BASE)
    Entry_Db= Entry(Frame_Entry_DATA_BASE)
    Entry_Table= Entry(Frame_Entry_DATA_BASE)    
    """"""""""""""""""


    
    Button_modificar=Button(modificar,text="Listo", command= lambda: func_1(modificar,[Entry_SMTP,Entry_PUERTO,Entry_DIRECCIÓN,Entry_PASSWORD,Entry_HOST,Entry_USER,Entry_DATA_BASE_PASSWORD,Entry_Db,Entry_Table]))
    
    #Colocar Widgets""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    vacio.grid(row=0,column=0,columnspan=2,sticky=W+E,padx=250)
    
    """"""""""""""""""
    Titulo_Correo.pack()
    
    Texto_SMTP.pack()
    Texto_PUERTO.pack()
    Texto_DIRECCIÓN.pack()
    Texto_PASSWORD.pack()
    
    Entry_SMTP.pack()
    Entry_PUERTO.pack()
    Entry_DIRECCIÓN.pack()
    Entry_PASSWORD.pack()
    """"""""""""""""""

    Titulo_DATA_BASE.pack()
    
    Texto_HOST.pack()
    Texto_USER.pack()
    Texto_DATA_BASE_PASSWORD.pack()
    Texto_Db.pack()
    Texto_Table.pack()
    
    Entry_HOST.pack()
    Entry_USER.pack()
    Entry_DATA_BASE_PASSWORD.pack()
    Entry_Db.pack()
    Entry_Table.pack()
    """"""""""""""""""    
    
    
    Button_modificar.grid(row=12,column=0,columnspan=2)
    
    
    
    #Iniciar Ventana
    modificar.mainloop()

def read_info():
    key=b'xMDD8sukJkSrRd_2q78M9vM8xJX87F4Kc-tS6Dgb2Cg='
    

    try:
        with open("./info/IBPC.txt","r") as f:
            f_2=Fernet(key)
            datos=f.readlines()
            datos=[f_2.decrypt(f_2.decrypt(a.strip().encode())).decode() for a in datos]  
          
    except:
        
        datos=["","","","","","",""]

    return datos

def guardar(app,datos):
    key=b'xMDD8sukJkSrRd_2q78M9vM8xJX87F4Kc-tS6Dgb2Cg='


    datos=[a.get() for a in datos]

    datos_old=read_info()
    with open("./info/IBPC.txt","w") as f:
        f_2=Fernet(key)
        for number in range(len(datos)):
            if datos[number]:   
                f.write(f_2.encrypt(f_2.encrypt(datos[number].encode())).decode()+"\n")
            else:
                f.write(f_2.encrypt(f_2.encrypt(datos_old[number].encode())).decode()+"\n")
                
    app.destroy()


def callback(url_list):
    for item in url_list:
        webbrowser.open_new(item)

def reset():
    global Attachments_base
    Entry_Subject.config(state='normal')
    Entry_Template.config(state='normal')
    Entry_Attachments.config(state='normal')
    #Entry_Db.config(state='normal')
    #Entry_Table.config(state='normal')

    Attachments_base=[]

    Entry_Subject.delete(0,END)
    
    #Entry_Template.delete(0,END)
    #Entry_Attachments.delete(0,END)
    #Entry_Db.delete(0,END)
    #Entry_Table.delete(0,END)
    #Boton_SI.config(state='active')
    #Boton_NO.config(state='active')
    
    
    Progress_bar.config(text="MOSTRARÁ EL PROGRESO UNA VEZ SE INICIE EL ENVIO")
    Warnings.config(text="AQUI SE MOSTRARÁN AVISOS")
    
    
    
def iniciar_envio(i,Subject,Template_name,Attachments_base,Attachment_personalizado,Warnings,Progress_bar,app):
    Entry_Subject.config(state='disabled')
    #Entry_Template.config(state='disabled')
    #Entry_Attachments.config(state='disabled')
    #Entry_Db.config(state='disabled')
    #Entry_Table.config(state='disabled')
    #Boton_SI.pack_forget()
    #Boton_NO.pack_forget()        
    Button_exit=Button(app,text="SALIR", command=app.destroy).grid(row=12,column=0)
    ENVIAR.run(i,Subject,Template_name,Attachments_base,Attachment_personalizado,Warnings,Progress_bar,app)    
    Button_reset=Button(app,text="RESET", command= reset).grid(row=12,column=1)
    
    



def new_att():
    global Entry_Attachments,Att
    filedir=filedialog.askopenfilename(initialdir="/", title="Elija el archivo deseado")
    print(filedir)
    filename=filedir.split('/')[-1]
    print(filename)
    try:        
        shutil.copyfile(filedir,"./info/Atts/"+filename)
        Entry_Attachments.destroy()
        Att=StringVar()
        Att.set("ELIJA UN ARCHIVO")
        Entry_Attachments= OptionMenu(Frame_Attachments,Att,*os.listdir("./info/Atts"))
        Entry_Attachments.grid(row=0,column=0,padx=125)
    except Exception as e:
        print(str(e))


# DEFINIR LA APP ######################################
app = Tk()
app.title("ENVIO DE CORREOS - CMI")
app.geometry("498x600")
#photo = PhotoImage(file = "base ema enhanced.png")
app.iconbitmap("./icons/CMI LOGO.ico")
#app.wm_iconphoto(False, photo)
##app.bind("<Escape>", lambda event: app.attributes("-fullscreen",not app.attributes("-fullscreen")))
#app.bind("<Escape>", lambda event: app.attributes("-fullscreen", False))
#app.attributes("-fullscreen", True) 
app.resizable(0,0)#######§
app_menu=Menu(app)
app.config(menu=app_menu)

#Definir Menus
Opciones=Menu(app_menu)
Opciones.add_command(label="MODIFICAR DATOS", command= lambda: modifier(guardar))
Opciones.add_separator()
Opciones.add_command(label="CREAR NUEVA PLANTILLA", command= lambda: WINDOW_OPENER.template_creator(read_info()))
Opciones.add_separator()
Opciones.add_command(label="MODIFICAR PLANTILLA EXISTENTE", command= lambda: WINDOW_OPENER.template_modifier())
Opciones.add_separator()
Opciones.add_command(label="AÑADIR NUEVO ADJUNTO", command= new_att)
Opciones.add_separator()
Opciones.add_command(label="EXIT", command= app.destroy)
app_menu.add_cascade(label="Opciones",menu=Opciones)


Info=Menu(app_menu)
Info.add_command(label="Leonardo Zambrano", command= lambda: callback(["https://www.instagram.com/zambranoema2001/"]))
Info.add_separator()
Info.add_command(label="CMI", command= lambda: callback(["https://cmiolimpiadas.com/","https://www.instagram.com/cmi_ecu/"]))
Info.add_separator()
app_menu.add_cascade(label="Info",menu=Info)

#Definir Frames
Frame_Basico=LabelFrame(app, text="",pady=10)
Frame_Texto_Basico=LabelFrame(app, text="",pady=30)
Frame_Entry_Basico=LabelFrame(app, text="",pady=26)

#Frame_MySQL=LabelFrame(app, text="",pady=10)
#Frame_Texto_MySQL=LabelFrame(app, text="",pady=30)
#Frame_Entry_MySQL=LabelFrame(app, text="",pady=32)


Frame_Attachments=LabelFrame(app, text="ATTACHMENTS",pady=10)
Frame_Personalizado=LabelFrame(Frame_Attachments, text="")

Frame_progress=LabelFrame(app, text="PROGRESO",pady=10)
Frame_warning=LabelFrame(app, text="AVISOS",pady=10)


#COLOCAR FRAMES
Frame_Basico.grid(row=1,column=0,columnspan=2,sticky=W+E)
Frame_Texto_Basico.grid(row=2,column=0,sticky=W+E)
Frame_Entry_Basico.grid(row=2,column=1,sticky=W+E)


#Frame_MySQL.grid(row=3,column=0,columnspan=2,pady=10,sticky=W+E)
#Frame_Texto_MySQL.grid(row=4,column=0,sticky=W+E)
#Frame_Entry_MySQL.grid(row=4,column=1,sticky=W+E)


Frame_Attachments.grid(row=5,column=0,columnspan=2,sticky=W+E)

Frame_Personalizado.grid(row=1,column=1,pady=10)
Frame_progress.grid(row=10,column=0,pady=0,columnspan=2,sticky=W+E)
Frame_warning.grid(row=11,column=0,columnspan=2,sticky=W+E)


# DEFINIR WIDGETS ######################################
vacio=Label(app,text="")
Titulo_Basico= Label(Frame_Basico, text="INFORMACIÓN BÁSICA DEL CORREO")
Texto_Subject=Label(Frame_Texto_Basico,text="Asunto del Correo")
Texto_Template=Label(Frame_Texto_Basico,text="Nombre de la Plantilla")


Entry_Subject= Entry(Frame_Entry_Basico)
Template=StringVar()
Template.set("ELIJA UNA PLANTILLA")
Entry_Template= OptionMenu(Frame_Entry_Basico,Template,*os.listdir("./info/Templates"))


#Titulo_MySQL= Label(Frame_MySQL, text="INFORMACIÓN SOBRE MySQL")


#Texto_Db=Label(Frame_Texto_MySQL,text="Nombre de la Base de Datos")
#Texto_Table=Label(Frame_Texto_MySQL,text="Nombre de la Tabla")


#Entry_Db= Entry(Frame_Entry_MySQL)
#Entry_Table= Entry(Frame_Entry_MySQL)

Attachments_base=[]
Att=StringVar()
Att.set("ELIJA UN ARCHIVO")
Entry_Attachments= OptionMenu(Frame_Attachments,Att,*os.listdir("./info/Atts"))


def add_atts(new):

    if new != "ELIJA UN ARCHIVO":
        if os.path.isdir("./info/Atts/"+new):
            Attachments_base.append(new+"/")
        else:
            Attachments_base.append(new)
    print(Attachments_base)
    Att.set("ELIJA UN ARCHIVO")

Add_Attachment=Button(Frame_Attachments,text="AÑADIR",command=lambda: add_atts(Att.get()))


Texto_Attachment_personalizado=Label(Frame_Attachments,text="¿Attachment Personalizado?")

Personalizado=BooleanVar()

    
Boton_SI=Radiobutton(Frame_Personalizado, text="SI",variable=Personalizado, value=True).pack()
Boton_NO=Radiobutton(Frame_Personalizado, text="NO",variable=Personalizado, value=False).pack()




Progress_bar=Label(Frame_progress,text="MOSTRARÁ EL PROGRESO UNA VEZ SE INICIE EL ENVIO",bd=1,wraplength=400,relief=SUNKEN)

Warnings=Label(Frame_warning,text="AQUI SE MOSTRARÁN AVISOS",wraplength=400,bd=1,relief=SUNKEN)
Warnings.config(width=70)
Button_run=Button(app,text="INICIAR ENVIO",command= lambda: iniciar_envio(read_info(),Entry_Subject.get(),Template.get(),Attachments_base,Personalizado.get(),Warnings,Progress_bar,app))

# COLOCAR WIDGETS ######################################
vacio.grid(row=0,column=0,columnspan=2,padx=246,pady=0,sticky=W+E)
Titulo_Basico.pack()
Texto_Subject.pack()
Texto_Template.pack()

Entry_Subject.pack()
Entry_Template.pack()

Entry_Attachments.grid(row=0,column=0,padx=125)
Entry_Attachments.config(width=20)
Add_Attachment.grid(row=0,column=1,sticky=W,pady=20)
Texto_Attachment_personalizado.grid(row=1,column=0)



Button_run.grid(row=12,column=0,columnspan=2)

Warnings.pack()
Progress_bar.pack()

# INICIAR LA APP ######################################
app.mainloop()



if __name__ == "__main__":
    pass

    #print(read_info())