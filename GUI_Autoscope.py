#####GUI para AutoscoPi#####

from tkinter import *
from motorA import motor

def getCoord():
    coordenadas = coord.get()
    continuar=mensaje(coordenadas)
    if continuar==True:
        motor(coordenadas)
        mensaje1()
    elif continuar==False:
        pass
    return coordenadas

def astroPREDEF():
    astro = astro1.get()
    if astro == "Sirio":
        coordenadas="06 45 8.17 -16 43 20.5"
    elif astro=="Canopus":
        coordenadas="06 23 57.15 -52 41 43.9"
    elif astro=="Arturo":
        coordenadas="14 15 38.47 +19 10 18"
    elif astro=="Alfa Centauri":
        coordenadas="14 39 30.69 -60 49 06.5"
    elif astro=="Vega":
        coordenadas="18 36 56.48 +38 47 07.3"
    elif astro=="Capella":
        coordenadas="05 16 41.6 +45 59 45"
    elif astro=="Rigel":
        coordenadas="05 14 32.28 -8 12 05.9"
    elif astro=="Proción":
        coordenadas="07 39 17.27 -47 23 17.3"
    elif astro=="Achernar":
        coordenadas="01 37 43.01 -57 14 13.4"
    elif astro=="Hadar":
        coordenadas="14 03 49.31 -60 22 22.7"
    elif astro=="Betelgeuse":
        coordenadas="05 55 10.35 +07 24 25.6"
    elif astro=="Altair":
        coordenadas="19 50 47.65 +08 52 12.8"
    elif astro=="Aldebarán":
        coordenadas="04 35 55.32 +16 30 30"
    elif astro=="Spica":
        coordenadas="13 25 11 -11 09 41.4"
    elif astro=="Antares":
        coordenadas="16 29 24.46 -26 25 55.7"
    elif astro=="Pollux":
        coordenadas="07 45 18.11 +28 01 31.4"
    elif astro=="Fomalhaut":
        coordenadas="22 57 39.47 -29 37 23.5"
    elif astro=="Deneb":
        coordenadas="20 41 25.92 +45 16 49.3"
    continuar=mensaje(coordenadas, astro)
    if continuar==True:
        motor(coordenadas)
        mensaje1()
    elif continuar==False:
        pass
    return coordenadas,astro

def openSTELLA():
    ####ABRIR STELLARIUM####
    mensaje1()
    
def HOME():
    #motor(coordenadas) ####
    mensaje1() 

def mensaje(coordenadas,astro="coordenadas"):
    continuar=messagebox.askokcancel("AutoscoPi v.0.1.0","Seleccionaste {}.\nSus coordenadas son:\n{}\n\n¿Mover telescopio?".format(astro, coordenadas))
    return continuar

def mensaje1():
    messagebox.showinfo("AutoscoPi v.0.1.0","¡Disfruta!")
    return 

ventana = Tk()
coord = StringVar()
astro1 = StringVar()
ventana.title("AutoscoPi v.0.1.0")
ventana.geometry("630x300")
ventana.config(bg="light blue")
Creator = Label(ventana,text="Creado por: Enrique Buendía",fg="purple4",bg="light blue").place(x=30,y=250)
coord.set("HH mm ss.ss +HH mm ss.ss")
ETQ= Label(ventana,text="Escribe las coordenadas del astro deseado:",fg="orange red",bg="light blue").place(x=30,y=30)
entrada = Entry(ventana,textvariable=coord,width=27,fg="gray60").place(x=310,y=30)
boton = Button(ventana,text="¡Listo!",command=getCoord,activeforeground="blue").place(x=535,y=30)
ETQ2= Label(ventana,text="O elige una de las opciones:",fg="orange red",bg="light blue").place(x=30,y=70)
opc=Spinbox(ventana,width=11,textvariable=astro1,values=("Sirio","Canopus","Alfa Centauri","Arturo","Vega","Capella","Rigel","Proción","Achernar","Hadar","Betelgeuse","Altair","Aldebarán","Spica","Antares","Pollux","Fomalhaut","Deneb")).place(x=210,y=70)
boton2=Button(ventana,text="¡Vamos!",command=astroPREDEF,activeforeground="blue").place(x=325,y=70)
ETQSTELLA= Label(ventana,text="Interctua con Stellarium:",fg="orange red",bg="light blue").place(x=30,y=110)
boton2=Button(ventana,text="Abrir",command=openSTELLA,activeforeground="blue").place(x=195,y=110)

iconHOME=PhotoImage(file="home.gif")
BOTONhome=Button(ventana,image=iconHOME,command=HOME,borderwidth=0,bg="light blue").place(x=30,y=150)
logoUAM = PhotoImage(file="uam.gif")
logoINAOE = PhotoImage(file="inaoe.gif")
LOGOuam=Label(ventana,image=logoUAM,borderwidth=0).place(x=455,y=223)
LOGOinaoe=Label(ventana,image=logoINAOE,borderwidth=0).place(x=535,y=220)
ventana.mainloop()
