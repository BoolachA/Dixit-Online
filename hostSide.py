from tkinter import *
from tkinter import messagebox
import socket, setting, subprocess, pyperclip, menu
from PIL import ImageTk, Image

def setConfigHost():
    hostVentana.attributes("-fullscreen", setting.FULLSCREEN)
    hostVentana.title(setting.TITLE)
    hostVentana.configure(bg=setting.COLOR3)
    hostVentana.geometry(setting.GEOMETRY)
    hostVentana.iconphoto(False, Dlogo)
    hostVentana.state('zoomed')

def ventanaCerrada():
    subprocess.Popen("TASKKILL /F /IM ServerDixitOnline.exe")
    hostVentana.destroy()
    menu.main()

def copiarIp():
    pyperclip.copy(setting.LOCALIP)
    messagebox.showinfo("Copiar IP","IP Copiado!")

def main():
    global hostVentana, Dlogo
    hostVentana = Tk()
    Dlogo = ImageTk.PhotoImage(Image.open("media/Dlogo.png"))
    setConfigHost()
    setting.LOCALIP = socket.gethostbyname(socket.gethostname())
    messagebox.showwarning("Juego local","Se creará un servidor local en este ordenador.")
    subprocess.Popen(["ServerDixitOnline.exe"])
    hostVentana.protocol("WM_DELETE_WINDOW", ventanaCerrada)
    ipLabel = Label(hostVentana, text=f"IP de la sala: {setting.LOCALIP}")
    ipLabel.pack()
    ipLabel.bind("<Button-1>", lambda e:copiarIp())
    hostVentana.mainloop()

if (__name__ == "__main__"):
    main()