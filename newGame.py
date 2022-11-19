from tkinter import *
from tkinter import messagebox
import socket
import setting

if(__name__=="__main__"):
    hostVentana = Tk()
    setting.LOCALIP = socket.gethostbyname(socket.gethostname())
    messagebox.showwarning("Juego local",f"Se creará un servidor en este ordenador, si no funciona correctamente pruebe desactivar el firewall del sistema.")
    hostVentana.mainloop()