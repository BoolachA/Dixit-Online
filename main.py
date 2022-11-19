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
    global textBottom
    logoLabel.pack(side=TOP, pady=40)
    startBtn.pack(pady=50)
    configBtn.pack()
    salirBtn.pack(pady=50)
    btnMenuConfig()
    textBottom = Label(text="Proyecto en fase de pruebas, fuciona solamente redes locales")
    textBottom.place(x=10,y=10)

def btnMenuConfig():
    arial = fuente.Font(family='Arial', size=30, weight='bold')
    salirBtn.configure(bg=setting.COLOR2, justify=CENTER, text="SALIR", activebackground=setting.COLOR1, height=1, width=20, font=arial, command=exit, fg=setting.COLOR1, borderwidth=0)
    configBtn.configure(bg=setting.COLOR2, justify=CENTER, text="PANTALLA COMPLETA", activebackground=setting.COLOR1, height=1, width=20, font=arial, command=toggleFullscreen, fg=setting.COLOR1, borderwidth=0)
    startBtn.configure(bg=setting.COLOR2, justify=CENTER, text="INICIAR JUEGO", activebackground=setting.COLOR1, height=1, width=20, font=arial, fg=setting.COLOR1, borderwidth=0, command=newGameRequest)
    


def newGameRequest():
    startBtn.configure(text="Crear sala", command=hostConfig)
    configBtn.configure(text="Entrar", command=" ")
    salirBtn.configure(text="Volver", command=btnMenuConfig)

def hostConfig():
    ventanaMenu.destroy()
    exec(open("newGame.py").read())

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
    logoLabel = Label(image=logo, borderwidth = 0, anchor=CENTER)
    startBtn = Button(ventanaMenu)
    configBtn = Button(ventanaMenu)
    salirBtn = Button(ventanaMenu)
    menu()
    ventanaMenu.bind("<Control-0>", exit)
    ventanaMenu.mainloop()