import time,os,shutil
from  watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
source='D:/Downloads'
destination='D:/Whitehatjr/class113/destination'
directorytree={
    "imageFiles":["jpg","png","jpeg","gif"],
    "vedioFiles":["mp4","mkv","avi","mpeg"],
    "documentFiles":["ppt","docx","txt","doc","pdf"]
}
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        name,extension=os.path.splitext(event.src_path)
        for key,value in directorytree.items():
            if extension in value:
                filename=os.path.basename(event.src_path)
                path1=source+"/"+filename
                path2=destination+"/"+key
                path3=destination+"/"+key+"/"+filename
                if os.path.exists(path2):
                    shutil.move(path1,path3)
                else:
                    os.mkdir(path2)
                    shutil.move(path1,path3)
event_handler=FileMovementHandler()
# initialing observer
observer=Observer()
# schedule the observer 
observer.schedule(event_handler,source,recursive=True)
try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()
