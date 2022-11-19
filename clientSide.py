from tkinter import *
import setting, menu, socket
from tkinter import simpledialog, messagebox
from PIL import ImageTk, Image

def setConfigClient():
    clientVentana.attributes("-fullscreen", setting.FULLSCREEN)
    clientVentana.title(setting.TITLE)
    clientVentana.configure(bg=setting.COLOR3)
    clientVentana.geometry(setting.GEOMETRY)
    clientVentana.iconphoto(False, Dlogo)
    clientVentana.state('zoomed')

def ventanaCerrada():
    clientVentana.destroy()
    menu.main()

def main():
    global clientVentana, Dlogo
    clientVentana = Tk()
    Dlogo = ImageTk.PhotoImage(Image.open("media/Dlogo.png"))
    setConfigClient()
    setting.LOCALIP = socket.gethostbyname(socket.gethostname())
    connectValidation = False
    while(connectValidation == False):
        serverIP = simpledialog.askstring("Introduzca IP", "Introduzca el IP de la sala: ")
        if(serverIP!=None):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                client.connect((serverIP, 60000))
            except:
                messagebox.showerror("Error", f"No ha sido posible conectarse al servidor {serverIP}")
        else:
            connectValidation=True
            ventanaCerrada()

    clientVentana.protocol("WM_DELETE_WINDOW", ventanaCerrada)
    clientVentana.mainloop()

if (__name__ == "__main__"):
    main()