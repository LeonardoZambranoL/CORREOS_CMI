# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:01:30 2020

@author: Leonardo
"""
from tkinter import *
import os
import MySQL_for_massive_mails


 
    
def template_creator(i):
    
    def save(i,app,Nombre,Plain,HTML):
        
        try:
            MySQL_for_massive_mails.add_column(i, Nombre)
            
            path_template="./info/Templates/"+Nombre
            os.mkdir(path_template)
            with open(path_template+"/PLAIN.txt","w") as file:
                file.write(Plain)
            with open(path_template+"/HTML.txt","w") as file:
                file.write(HTML)
                
                
            path_register="./Register/"+Nombre
            os.mkdir(path_register)
            with open(path_register+"/YA ENVIADO.txt","w") as file:
                pass
            with open(path_register+"/NO ENVIADO.txt","w") as file:
                pass
            
            
        except Exception as e:
            print(str(e))
        

        app.destroy()
        return
        
        
        
    creator = Toplevel()
    creator.title("PLANTILLA NUEVA - CMI")
    creator.geometry("1205x620")
    creator.iconbitmap("./icons/PLUS.ico")
    creator.bind("<Escape>", lambda event: creator.attributes("-fullscreen",not creator.attributes("-fullscreen")))
    ##creator.resizable(0,0)
    #scrollbar =Scrollbar(orient="horizontal")
    #Definir Frames""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""
    Frame_Titulo=LabelFrame(creator, text="",pady=10)
    Frame_Aviso=LabelFrame(creator, text="",pady=10)
    Frame_Name=LabelFrame(creator, text="",pady=10)
    Frame_Plain=LabelFrame(creator, text="",pady=10)
    Frame_HTML=LabelFrame(creator, text="",pady=10)
    
    
    
    #Colocar Frames""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""
    Frame_Titulo.grid(row=1,column=0,columnspan=2,sticky=W+E)
    Frame_Aviso.grid(row=2,column=0,columnspan=2,sticky=W+E)
    Frame_Name.grid(row=3,column=0,columnspan=2,sticky=W+E)
    Frame_Plain.grid(row=4,column=0,sticky=W+E)
    Frame_HTML.grid(row=4,column=1,sticky=W+E)
    
    
    #Definir Widgets""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #vacio=Label(creator,text="")
    Texto_Tittle=Label(Frame_Titulo,text="INTRODUCIR INFORMACIÓN SOBRE LA NUEVA PLANTILLA (EVITAR CARACTERES ESPECIALES)")
    Texto_Aviso=Label(Frame_Aviso,text="Esta plantilla se creará para : "+i[7]+"."+i[8]+"\nSi desea que la plantilla sirva para otra tabla o base de datos, cierre esta ventana, modifique la informacion desde la app principal y vuelva a intentar\n")
    Texto_Plain=Label(Frame_Plain,text="Texto plano")
    Texto_HTML=Label(Frame_HTML,text="Texto formateado en HTML")
    
    
    """""""""""""""""" 
    Texto_Name=Label(Frame_Name,text="Nombre de la nueva plantilla : ")
    Entry_Name=Entry(Frame_Name,justify=CENTER)
    Entry_Plain=Text(Frame_Plain,highlightcolor="yellow",highlightthickness=1,width=74,height=21)
    Entry_HTML=Text(Frame_HTML,highlightcolor="yellow",highlightthickness=1,width=74,height=21)
    """"""""""""""""""
    
    Button_save=Button(creator,text="Listo",font=("Times New Roman",12),command= lambda: save(i,creator,Entry_Name.get(),Entry_Plain.get(1.0 , END),Entry_HTML.get(1.0 , END)))
    
    #Colocar Widgets""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #vacio.grid(row=0,column=0,columnspan=2,sticky=W+E,padx=1)
    Texto_Tittle.pack()
    Texto_Aviso.pack()
    Texto_Name.grid(row=0,column=0, padx=320)
    Entry_Name.place(x=500, y=1, width=300)
    Texto_Plain.pack()
    Texto_HTML.pack()
    Entry_Plain.pack()
    Entry_HTML.pack()
    Button_save.grid(row=20,column=0,columnspan=2,ipadx=30,ipady=10)
    #Iniciar ventana""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""22
    creator.mainloop()    
    return




def template_modifier():
    modifier = Toplevel()
    modifier.title("MODIFICAR PLANTILLA - CMI")
    modifier.geometry("1205x620")
    modifier.iconbitmap("./icons/PLUS.ico")
    modifier.bind("<Escape>", lambda event: modifier.attributes("-fullscreen",not modifier.attributes("-fullscreen")))
    
    #Definir Frames""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""
    Frame_Titulo=LabelFrame(modifier, text="",pady=10)
    Frame_Aviso=LabelFrame(modifier, text="",pady=10)
    Frame_Name=LabelFrame(modifier, text="",pady=10)
    Frame_Plain=LabelFrame(modifier, text="",pady=10)
    Frame_HTML=LabelFrame(modifier, text="",pady=10)
    
    
    #Colocar Frames""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""
    Frame_Titulo.grid(row=1,column=0,columnspan=2,sticky=W+E)
    Frame_Aviso.grid(row=2,column=0,columnspan=2,sticky=W+E)
    Frame_Name.grid(row=3,column=0,columnspan=2,sticky=W+E)
    Frame_Plain.grid(row=4,column=0,sticky=W+E)
    Frame_HTML.grid(row=4,column=1,sticky=W+E)
 
    #Definir Widgets""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #vacio=Label(creator,text="")
    Texto_Tittle=Label(Frame_Titulo,text="ELIJA UNA PLANTILLA Y MODIFIQUELA")
    Texto_Aviso=Label(Frame_Aviso,text="AQUI SE MOSTRARÁN AVISOS",wraplength=1000)
    Texto_Plain=Label(Frame_Plain,text="Texto plano")
    Texto_HTML=Label(Frame_HTML,text="Texto formateado en HTML")


    
    """""""""""""""""" 
    Texto_Name=Label(Frame_Name,text="Elija la plantilla a modificar : ")
    Selected_template=StringVar()
    Selected_template.set("ELIJA UNA PLANTILLA")
    Template_list=OptionMenu(Frame_Name,Selected_template,*os.listdir("./info/Templates"))
    
    modifying=".@&@."
    def select(template,Entry_Plain, Entry_HTML):
        global modifying
        Entry_Plain.config(state="normal")
        Entry_HTML.config(state="normal")
        Entry_Plain.delete(1.0, END)
        Entry_HTML.delete(1.0, END) 
        modifying=template
        template_dir="./info/Templates/"+modifying
        plain_dir=template_dir+"/PLAIN.txt"
        HTML_dir=template_dir+"/HTML.txt"
        Entry_Plain.insert(END,"cargando...")
        Entry_HTML.insert(END,"cargando...")
        modifier.update()
        Texto_Aviso.config(text="moficando : "+modifying)
       
        try:
            with open(plain_dir,"r") as plain:
                contents=plain.read()
                Entry_Plain.delete(1.0, END)
                Entry_Plain.insert(END,contents)
            with open(HTML_dir,"r") as HTML:
                contents=HTML.read()
                Entry_HTML.delete(1.0, END)
                Entry_HTML.insert(END,contents)    
                
        except Exception as e:
            Entry_Plain.config(state="disabled")
            Entry_HTML.config(state="disabled")
            Texto_Aviso.config(text=str(e))

    
    Button_select=Button(Frame_Name,text="Elegir",command= lambda: select(Selected_template.get(),Entry_Plain, Entry_HTML))
    Entry_Plain=Text(Frame_Plain,highlightcolor="yellow",highlightthickness=1,width=74,height=21)
    Entry_HTML=Text(Frame_HTML,highlightcolor="yellow",highlightthickness=1,width=74,height=21)
    Entry_Plain.config(state="disabled")
    Entry_HTML.config(state="disabled")
    """"""""""""""""""
    
    def save(app,Plain,HTML):
        global modifying
        template_dir="./info/Templates/"+modifying
        plain_dir=template_dir+"/PLAIN.txt"
        HTML_dir=template_dir+"/HTML.txt"        
        try:
            with open(plain_dir,"w") as plain_file:
                print("in open",plain_dir)
                plain_file.write(Plain)
            with open(HTML_dir,"w") as HTML_file:
                HTML_file.write(HTML)
            Texto_Aviso.config(text="LOS CAMBIOS FUERON GUARDADOS")
            app.update()
            app.after(2000)
            app.destroy()       
        except Exception as e:
            print(str(e))
            Texto_Aviso.config(text=str(e))        
        
        
        
        
        
    Button_save=Button(modifier,text="Listo",font=("Times New Roman",12),command= lambda: save(modifier,Entry_Plain.get(1.0 , END),Entry_HTML.get(1.0 , END)))
    
    #Colocar Widgets""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #vacio.grid(row=0,column=0,columnspan=2,sticky=W+E,padx=1)
    Texto_Tittle.pack()
    Texto_Aviso.pack()
    Texto_Name.grid(row=0,column=0, padx=320)
    Template_list.place(x=520,y=-2)
    Button_select.grid(row=0,column=2)
    Texto_Plain.pack()
    Texto_HTML.pack()
    Entry_Plain.pack()
    Entry_HTML.pack()
    Button_save.grid(row=20,column=0,columnspan=2,ipadx=30,ipady=10)
    #Iniciar ventana""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""22
    
    
    
    
    modifier.mainloop() 


""" INTENTO DE CREAR UNA CLASE QUE COMPRENDA MODIFIER Y CREATOR; NO TENGO MUCHO TIEMPO ASI Q SEGUIRÉ CON EL CÓDIGO DE ARRIBA 

class Template_worker:
    def __init__(self):
        worker = Toplevel()
        worker.title("PLANTILLA NUEVA - CMI")
        worker.geometry("1205x620")
        worker.iconbitmap("./icons/PLUS.ico")
        worker.bind("<Escape>", lambda event: worker.attributes("-fullscreen",not worker.attributes("-fullscreen")))
        ##creator.resizable(0,0)
        scrollbar =Scrollbar(orient="horizontal")
        #Definir Frames""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """"""""""""""""""
        Frame_Titulo=LabelFrame(worker, text="",pady=10)
        Frame_Aviso=LabelFrame(worker, text="",pady=10)
        Frame_Name=LabelFrame(worker, text="",pady=10)
        Frame_Plain=LabelFrame(worker, text="",pady=10)
        Frame_HTML=LabelFrame(worker, text="",pady=10)
        
        
        
        #Colocar Frames""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """"""""""""""""""
        Frame_Titulo.grid(row=1,column=0,columnspan=2,sticky=W+E)
        Frame_Aviso.grid(row=2,column=0,columnspan=2,sticky=W+E)
        Frame_Name.grid(row=3,column=0,columnspan=2,sticky=W+E)
        Frame_Plain.grid(row=4,column=0,sticky=W+E)
        Frame_HTML.grid(row=4,column=1,sticky=W+E)
        
        
        #Definir Widgets""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #vacio=Label(creator,text="")
        Texto_Tittle=Label(Frame_Titulo,text="INTRODUCIR INFORMACIÓN SOBRE LA NUEVA PLANTILLA (EVITAR CARACTERES ESPECIALES)")
        Texto_Aviso=Label(Frame_Aviso,text="Esta plantilla se creará para : "+i[7]+"."+i[8]+"\nSi desea que la plantilla sirva para otra tabla o base de datos, cierre esta ventana, modifique la informacion desde la app principal y vuelva a intentar\n")
        Texto_Plain=Label(Frame_Plain,text="Texto plano")
        Texto_HTML=Label(Frame_HTML,text="Texto formateado en HTML")
        
        
        """""""""""""""""" 
        Texto_Name=Label(Frame_Name,text="Nombre de la nueva plantilla : ")
        Entry_Name=Entry(Frame_Name,justify=CENTER)
        Entry_Plain=Text(Frame_Plain,highlightcolor="yellow",highlightthickness=1,width=74,height=21)
        Entry_HTML=Text(Frame_HTML,highlightcolor="yellow",highlightthickness=1,width=74,height=21)
        """"""""""""""""""
        #lambda: save(i,creator,Entry_Name.get(),Entry_Plain.get(1.0 , END),Entry_HTML.get(1.0 , END),option,frame,Template)
        Button_save=Button(worker,text="Listo",font=("Times New Roman",12),command= self.save_new(i,Entry_Name.get(),Entry_Plain.get(1.0 , END),Entry_HTML.get(1.0 , END),option,frame,Template))
        
        #Colocar Widgets""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #vacio.grid(row=0,column=0,columnspan=2,sticky=W+E,padx=1)
        Texto_Tittle.pack()
        Texto_Aviso.pack()
        Texto_Name.grid(row=0,column=0, padx=320)
        Entry_Name.place(x=500, y=1, width=300)
        Texto_Plain.pack()
        Texto_HTML.pack()
        Entry_Plain.pack()
        Entry_HTML.pack()
        Button_save.grid(row=20,column=0,columnspan=2,ipadx=30,ipady=10)
        #Iniciar ventana""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""22
        worker.mainloop()        
        
        def save_new(self,i,app,Nombre,Plain,HTML,option,frame,Template):
            try:
                MySQL_for_massive_mails.add_column(i, Nombre)
                
                path_template="./info/Templates/"+Nombre
                os.mkdir(path_template)
                with open(path_template+"/PLAIN.txt","w") as file:
                    file.write(Plain)
                with open(path_template+"/HTML.txt","w") as file:
                    file.write(HTML)
                    
                    
                path_register="./Register/"+Nombre
                os.mkdir(path_register)
                with open(path_register+"/YA ENVIADO.txt","w") as file:
                    pass
                with open(path_register+"/NO ENVIADO.txt","w") as file:
                    pass
                
                
            except Exception as e:
                print(str(e))
            
            option.destroy()
            Template=StringVar()
            Template.set("ELIJA UNA PLANTILLA")
            option=OptionMenu(frame,Template,*os.listdir("./info/Templates"))
            option.pack()
            self.destroy()
            return
"""
if __name__ == "__main__":
    
    template_modifier()