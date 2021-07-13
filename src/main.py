#!/usr/bin/python
import time
import os
from datetime import datetime, timedelta
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path


class ClashConfigFileHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = datetime.now()
        self.__is_writing__ = False

    def on_modified(self, event):
        if self.__is_writing__:
            return

        if event.is_directory:
            return

        fname = os.path.basename(event.src_path)

        if not fname.endswith(".yaml"):
            return

        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()

        with open(event.src_path, "r+") as f:
            content = f.readlines()
            content.insert(-4, "# by Q.s. \n")
            content.insert(-4, "- IP-CIDR,190.190.190.0/24,DIRECT \n")
            content.insert(-4, "\n")

            self.__is_writing__ = True
            for line in content:
                f.write(str(line))
            self.__is_writing__ = False


if __name__ == "__main__":
    event_handler = ClashConfigFileHandler()
    observer = Observer()
    observer.schedule(
        event_handler, path=str(Path.home()) + "/.config/clash", recursive=False
    )
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
