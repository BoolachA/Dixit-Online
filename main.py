import eel, os, subprocess, socket, client
#import ctypes
#ctypes.windll.user32.MessageBoxW(0, "message", "title", "icon"16)

def salir(*kw):
    os.system("taskkill /f /im server.py")
    os._exit(0)

@eel.expose
def configHost(stage):
    if(stage =="shutdown"):
        os.system("taskkill /f /im server.py")
    elif(stage == "startup"):
        eel.showScreen("GameLobby")
        print("Starting server as subprocess...")
        subprocess.Popen("server.py")

@eel.expose
def startClient(ip):
    client.IP = ip
    client.main()

def main():
    eel.init('web')
    eel.start('index.html', close_callback=salir)

@eel.expose
def getHostIp():
    localip = socket.gethostbyname(socket.gethostname())
    return localip

if __name__ == "__main__":
    main()