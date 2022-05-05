import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "INGRESA LA RUTA DE LA CARPETA DESCARGAS (UTILIZA " / ") en VSC"
# to_dir = "INGRESA LA RUTA DE LA CARPETA DESTINO(UTILIZA " / ") en VSC"

from_dir = "C:/Users/preet/Downloads"
to_dir = "C:/Users/preet/Desktop/Downloaded_Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Clase event handler 

class FileMovementHandler(FileSystemEventHandler):

    #Actividad del alumno1

    

    def on_created(self, event):
        print(event)
        print(event.src_path)


# Inicia la clase event handler
event_handler = FileMovementHandler()


# Inicia Observer
observer = Observer()

# Programa el Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicia el Observer
observer.start()

#Actividad del alumno 2
while True:
    time.sleep(2)
    print("ejecutando...")

    
