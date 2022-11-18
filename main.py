from tkinter import *
from PIL import ImageTk, Image
import setting
import tkinter.font as fuente

ventanaMenu=Tk()

def setConfig():
    ventanaMenu.attributes("-fullscreen", setting.FULLSCREEN)
    ventanaMenu.title(setting.TITLE)
    ventanaMenu.configure(bg=setting.COLOR3)
    ventanaMenu.geometry(setting.GEOMETRY)
    ventanaMenu.state('zoomed')
    

def menu():
    arial = fuente.Font(family='Arial', size=30, weight='bold')
    logoLabel = Label(image=logo, borderwidth = 0, anchor=CENTER).pack(side=TOP, pady=40)
    startBtn = Button(ventanaMenu, bg=setting.COLOR2, justify=CENTER, text="INICIAR JUEGO", activebackground=setting.COLOR1,
     height=1, width=20, font=arial, fg=setting.COLOR1, borderwidth=0).pack(pady=50)
    configBtn = Button(ventanaMenu, bg=setting.COLOR2, justify=CENTER, text="PANTALLA COMPLETA", activebackground=setting.COLOR1,
     height=1, width=20, font=arial, command=toggleFullscreen, fg=setting.COLOR1, borderwidth=0).pack()
    salirBtn = Button(ventanaMenu, bg=setting.COLOR2, justify=CENTER, text="SALIR", activebackground=setting.COLOR1,
     height=1, width=20, font=arial, command=exit, fg=setting.COLOR1, borderwidth=0).pack(pady=50)

def ajustesScreen():
    ventanaConfig=Tk()

def toggleFullscreen():
    if(setting.FULLSCREEN==False):
        setting.FULLSCREEN=True
    else:
        setting.FULLSCREEN=False
    setConfig()

if __name__ == "__main__":
    logo = ImageTk.PhotoImage(Image.open("media/logo.jpg"))
    setConfig()
    menu()
    ventanaMenu.mainloop()