from tkinter import *
from tkinter import messagebox
import socket, setting, sys, server
from PIL import ImageTk, Image

def setConfigHost():
    hostVentana.attributes("-fullscreen", setting.FULLSCREEN)
    hostVentana.title(setting.TITLE)
    hostVentana.configure(bg=setting.COLOR3)
    hostVentana.geometry(setting.GEOMETRY)
    hostVentana.iconphoto(False, Dlogo)
    hostVentana.state('zoomed')

def setupHost():
    global hostVentana, Dlogo
    hostVentana = Tk()
    hostVentana.bind("<Control-0>", sys.exit)
    Dlogo = ImageTk.PhotoImage(Image.open("media/Dlogo.png"))
    setConfigHost()
    setting.LOCALIP = socket.gethostbyname(socket.gethostname())
    messagebox.showwarning("Juego local","Se creara un servidor local en este ordenador.")
    server.main()
    hostVentana.mainloop()

if __name__ == "__main__":
    setupHost()