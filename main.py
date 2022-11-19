from tkinter import *
from PIL import ImageTk, Image
import setting
import tkinter.font as fuente

def setConfig():
    ventanaMenu.attributes("-fullscreen", setting.FULLSCREEN)
    ventanaMenu.title(setting.TITLE)
    ventanaMenu.configure(bg=setting.COLOR3)
    ventanaMenu.geometry(setting.GEOMETRY)
    ventanaMenu.iconphoto(False, Dlogo)
    ventanaMenu.state('zoomed')
    

def menu():
    global logoLabel, startBtn, configBtn, salirBtn, textBottom
    arial = fuente.Font(family='Arial', size=30, weight='bold')
    logoLabel = Label(image=logo, borderwidth = 0, anchor=CENTER)
    logoLabel.pack(side=TOP, pady=40)
    startBtn = Button(ventanaMenu, bg=setting.COLOR2, justify=CENTER, text="INICIAR JUEGO", activebackground=setting.COLOR1,
     height=1, width=20, font=arial, fg=setting.COLOR1, borderwidth=0, command=newGameRequest)
    startBtn.pack(pady=50)
    configBtn = Button(ventanaMenu, bg=setting.COLOR2, justify=CENTER, text="PANTALLA COMPLETA", activebackground=setting.COLOR1,
     height=1, width=20, font=arial, command=toggleFullscreen, fg=setting.COLOR1, borderwidth=0)
    configBtn.pack()
    salirBtn = Button(ventanaMenu, bg=setting.COLOR2, justify=CENTER, text="SALIR", activebackground=setting.COLOR1,
     height=1, width=20, font=arial, command=exit, fg=setting.COLOR1, borderwidth=0)
    salirBtn.pack(pady=50)
    textBottom = Label(text="Proyecto de Eduardo Vieira")
    textBottom.place(x=10,y=10)

def newGameRequest():
    logoLabel.destroy();startBtn.destroy();configBtn.destroy();salirBtn.destroy();textBottom.destroy()

    print("hola")

def ajustesScreen():
    ventanaConfig=Tk()

def toggleFullscreen():
    if(setting.FULLSCREEN==False):
        setting.FULLSCREEN=True
    else:
        setting.FULLSCREEN=False
    setConfig()

if __name__ == "__main__":
    ventanaMenu = Tk()
    Dlogo = ImageTk.PhotoImage(Image.open("media/Dlogo.png"))
    logo = ImageTk.PhotoImage(Image.open("media/logo.jpg"))
    setConfig()
    menu()
    ventanaMenu.bind("<Control-0>", exit)
    ventanaMenu.mainloop()