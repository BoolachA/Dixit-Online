import eel, os, subprocess
#import ctypes
#ctypes.windll.user32.MessageBoxW(0, "message", "title", "icon"16)

def salir(*kw):
    os.system("taskkill /f /im ServerDixitOnline.exe")
    os._exit(0)


@eel.expose
def configHost(stage):
    if(stage =="shutdown"):
        os.system("taskkill /f /im ServerDixitOnline.exe")
    elif(stage == "startup"):
        print("Starting server as subprocess...")
        subprocess.Popen("ServerDixitOnline.exe")

def main():
    eel.init('web')
    eel.start('index.html', close_callback=salir)

if __name__ == "__main__":
    main()