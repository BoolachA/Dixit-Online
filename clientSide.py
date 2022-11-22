from tkinter import *
import setting, menu, socket
from tkinter import simpledialog, messagebox, scrolledtext
from PIL import ImageTk, Image

def setConfigClient():
    clientVentana.attributes("-fullscreen", setting.FULLSCREEN)
    clientVentana.title(setting.TITLE)
    clientVentana.configure(bg=setting.COLOR3)
    clientVentana.geometry(setting.GEOMETRY)
    clientVentana.iconphoto(False, Dlogo)
    logoLabel.pack(side=TOP)
    clientVentana.state('zoomed')

def ventanaCerrada():
    clientVentana.destroy()
    #menu.main()

def configLobby():
    chatbox.configure(width=100, height=30, bg=setting.COLOR4)
    playerList.configure(width=70, height=30, bg=setting.COLOR4)
    chatbox.place(x=((clientVentana.winfo_width()/4)-chatbox.winfo_reqwidth()/2.3), y=200)
    #print(clientVentana.winfo_)
    playerList.place(x=((clientVentana.winfo_width()/2)-playerList.winfo_reqwidth()/2), y=200)

    pass

def main():
    # while True: print("tumama")
    global clientVentana, Dlogo, chatbox, logoLabel, playerList
    clientVentana = Tk()
    Dlogo = ImageTk.PhotoImage(Image.open("media/Dlogo.png"))
    logo = ImageTk.PhotoImage(Image.open("media/logo2.jpg"))
    logoLabel = Label(image=logo, borderwidth = 0, anchor=CENTER)
    chatbox = scrolledtext.ScrolledText()
    playerList = scrolledtext.ScrolledText()
    setConfigClient()
    configLobby()
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