import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from PIL import Image, ExifTags

sys.path.append("../")

if __name__ == "__main__":
    # path = sys.argv[1]
    patterns = ["*.jpg", "*.JPG"]
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True

    # istanzio un handler
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


    def on_created(event):
        # print(f"hey, {event.src_path} has been created!")
        # comando = "python3 comprimi.py " + event.src_path
        # os.system(comando)
        os.system("python3 comprimi.py " + event.src_path)
        # print(f"hey, {event.src_path} has been compressed!")


    def on_deleted(event):
        # print(f"what the f**k! Someone deleted {event.src_path}!")
        pass


    def on_modified(event):
        # print(f"hey buddy, {event.src_path} has been modified")
        pass


    def on_moved(event):
        # print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
        pass


    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    path = "."
    go_recursively = False

    # istanzio l'observer
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
