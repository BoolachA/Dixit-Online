from tkinter import *
from PIL import ImageTk, Image
import setting, sys, newGame
import tkinter.font as fuente

def setConfigMenu():
    ventanaMenu.attributes("-fullscreen", setting.FULLSCREEN)
    ventanaMenu.title(setting.TITLE)
    ventanaMenu.configure(bg=setting.COLOR3)
    ventanaMenu.geometry(setting.GEOMETRY)
    ventanaMenu.iconphoto(False, Dlogo)
    ventanaMenu.state('zoomed')    

def menu():
    logoLabel.pack(side=TOP, pady=40)
    startBtn.pack(pady=50)
    configBtn.pack()
    salirBtn.pack(pady=50)
    btnMenuConfig()
    textBottom = Label(text="Proyecto en fase de pruebas, fuciona solamente redes locales")
    textBottom.place(x=10,y=10)

def btnMenuConfig():
    arial = fuente.Font(family='Arial', size=30, weight='bold')
    salirBtn.configure(bg=setting.COLOR2, justify=CENTER, text="SALIR", activebackground=setting.COLOR1, height=1, width=20, font=arial, command=sys.exit, fg=setting.COLOR1, borderwidth=0)
    configBtn.configure(bg=setting.COLOR2, justify=CENTER, text="PANTALLA COMPLETA", activebackground=setting.COLOR1, height=1, width=20, font=arial, command=toggleFullscreen, fg=setting.COLOR1, borderwidth=0)
    startBtn.configure(bg=setting.COLOR2, justify=CENTER, text="INICIAR JUEGO", activebackground=setting.COLOR1, height=1, width=20, font=arial, fg=setting.COLOR1, borderwidth=0, command=newGameRequest)

def newGameRequest():
    startBtn.configure(text="Crear sala", command=hostConfig)
    configBtn.configure(text="Entrar", command=" ")
    salirBtn.configure(text="Volver", command=btnMenuConfig)

def hostConfig():
    ventanaMenu.destroy()
    newGame.setupHost()
    
def toggleFullscreen():
    if(setting.FULLSCREEN==False):
        setting.FULLSCREEN=True
    else:
        setting.FULLSCREEN=False
    setConfigMenu()

def main():
    global ventanaMenu, Dlogo, logo, logoLabel, startBtn, configBtn, salirBtn
    ventanaMenu = Tk()
    Dlogo = ImageTk.PhotoImage(Image.open("media/Dlogo.png"))
    logo = ImageTk.PhotoImage(Image.open("media/logo.jpg"))
    setConfigMenu()
    logoLabel = Label(image=logo, borderwidth = 0, anchor=CENTER)
    startBtn = Button(ventanaMenu)
    configBtn = Button(ventanaMenu)
    salirBtn = Button(ventanaMenu)
    menu()
    ventanaMenu.bind("<Control-0>", sys.exit)
    ventanaMenu.mainloop()

if __name__ == "__main__":
    main()