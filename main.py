import eel, os, subprocess, socket, client
#import ctypes
#ctypes.windll.user32.MessageBoxW(0, "message", "title", "icon"16)

def salir(*kw):
    client.RunninigClient=False
    os._exit(0)

@eel.expose
def configHost(stage):
    if(stage =="shutdown"):
        client.RunninigClient=False
    elif(stage == "startup"):
        eel.showScreen("GameLobby")
        print("Starting server as subprocess...")
        subprocess.Popen("server.py")

@eel.expose
def startClient(ip):
    client.main()
    #subprocess.call(['python client.py'])

def main():
    eel.init('web')
    eel.start('index.html', close_callback=salir)

@eel.expose
def getHostIp():
    localip = socket.gethostbyname(socket.gethostname())
    return localip


if __name__ == "__main__":
    main()