from tkinter import *
from tkinter import messagebox
import socket, setting, sys, subprocess
from PIL import ImageTk, Image

def setConfigHost():
    hostVentana.attributes("-fullscreen", setting.FULLSCREEN)
    hostVentana.title(setting.TITLE)
    hostVentana.configure(bg=setting.COLOR3)
    hostVentana.geometry(setting.GEOMETRY)
    hostVentana.iconphoto(False, Dlogo)

def ventanaCerrada():
    subprocess.Popen("TASKKILL /F /IM " + "ServerDixitOnline.exe")
    hostVentana.destroy()
    sys.exit()

def setupHost():
    global hostVentana, Dlogo, p
    hostVentana = Tk()
    Dlogo = ImageTk.PhotoImage(Image.open("media/Dlogo.png"))
    setConfigHost()
    setting.LOCALIP = socket.gethostbyname(socket.gethostname())
    messagebox.showwarning("Juego local","Se creara un servidor local en este ordenador.")
    p = subprocess.Popen(["ServerDixitOnline.exe"])
    hostVentana.bind("<Control-0>", sys.exit)
    hostVentana.protocol("WM_DELETE_WINDOW", ventanaCerrada)
    hostVentana.state('zoomed')
    hostVentana.mainloop()

if __name__ == "__main__":
    setupHost()