import eel, os, subprocess, socket, client, threading
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
    hiloClient = threading.Thread(target=client.main())
    hiloClient.start()

def main():
    eel.init('web')
    eel.start('index.html', close_callback=salir)

@eel.expose
def getHostIp():
    localip = socket.gethostbyname(socket.gethostname())
    return localip

class thread_with_trace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        # sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == "call":
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == "line":
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed=True


if __name__ == "__main__":
    main()