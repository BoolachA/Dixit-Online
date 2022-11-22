import eel, os
#import ctypes
#ctypes.windll.user32.MessageBoxW(0, "message", "title", "icon"16)

def salir(*kw):
    os._exit(0)

eel.init('web')
eel.start('index.html', close_callback=salir)