from tkinter import * #Importar libreria
raiz=Tk()
import pygame,sys 
from pygame.locals import*
from tkinter import filedialog
from PIL import ImageTk,Image



pygame.init()#Este metodo inicia la libreria pygame
    
def OpenSong():
    Song= filedialog.askopenfilename()
    print(Song)
    pygame.mixer.music.load(Song)

    pass

def PlaySong():
    pygame.mixer.music.play()
    pass

def StopSong():
    pygame.mixer.music.stop()
    pass

def ResumeSong():
    pygame.mixer.music.unpause()
    pass

def PauseSong():
    pygame.mixer.music.pause()
    pass

def VolumUpper():
    nivelVolumen= pygame.mixer.music.get_volume()+0.7
    pygame.mixer.music.set_volume(nivelVolumen)
    
def VolumLower():
    nivelVolumen=pygame.mixer.music.get_volume()-0.7
    pygame.mixer.music.set_volume(nivelVolumen)


raiz.title("Reproductor")
#raiz.iconbitmap("gato.ico")#cambia el icono de la pantalla 
raiz.geometry("1000x500")
raiz.resizable(1,1)

#frame o marco
framePrincipal= Frame(raiz,bg="#4d4d4d",width=600, height=400)
framePrincipal.pack(fil="both", expand=1)


#imagen
im=Image.open("Amoveresecuerpo.jpg")
imRe=im.resize((200,150))
imagen=ImageTk.PhotoImage(imRe)

imlabel=Label(framePrincipal,image=imagen)
imlabel.place(relx=0.4,rely=0.12)


#Titulo reprodeucor
TituloReproductor=Label(framePrincipal,text="Reproductor GUI", font=("Jokerman",20),bg="#4d4d4d",fg="#f4f4f4")# , despues del tamaño de fuente pone una tipografia(negritas, subrayado, etc)
TituloReproductor.pack()

#Boton Open File
BotonOpenFile=Button(framePrincipal,text="Open File",font=("Jokerman",20),bg="#5dc460"
                     ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=OpenSong)#Command llama la funcion Opensong que pregunta por la direccion de un archivo
BotonOpenFile.place(relx=0.05,rely=0.5)#relx y relycoloca en coordenads por porcentaje(.1=10% de la ventana o frame)


#BotonPlay
BotonPlay=Button(framePrincipal,text="Play",font=("Jokerman",20),bg="#5dc460"
                     ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=PlaySong)
BotonPlay.place(relx=0.25,rely=0.5)

#BotonPause
BotonPause=Button(framePrincipal,text="Pause",font=("Jokerman",20),bg="#ad21da"
                     ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=PauseSong)
BotonPause.place(relx=0.45,rely=0.5)

#BotonResume
BotonResm=Button(framePrincipal,text="Resume",font=("Jokerman",20),bg="#334eaf"
                     ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=ResumeSong)
BotonResm.place(relx=0.65,rely=0.5)

#Boton Stop
BotonStop=Button(framePrincipal,text="Stop",font=("Jokerman",20),bg="#4f5f6f"
                     ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=StopSong)
BotonStop.place(relx=0.85,rely=0.5)

#BotonVolumenUpper
BotonVUP=Button(framePrincipal,text="Vupper",font=("Jokerman",20),bg="#334eaf"
                     ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=VolumUpper)
BotonVUP.place(relx=0.65,rely=0.8)

#Boton VolumenLower
BotonVL=Button(framePrincipal,text="Vlower",font=("Jokerman",20),bg="#4f5f6f"
                     ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=VolumLower)
BotonVL.place(relx=0.85,rely=0.8)




raiz.mainloop()