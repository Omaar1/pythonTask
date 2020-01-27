import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import  myBanner
from makeAchoice import makeAchoice


def run():
    auditList = ["#-------------- Directory Auditor --------------#", "1. Save output to file (watchdog.log)",
     "2. Pipe output to terminal"]
    path = input("Directory Full Path: ")
    inp = makeAchoice(auditList, 2)
    if(inp == 1):
        logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                        filename="./watchdog.txt")
    else:
        logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    try:
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
    except:
        print("ERROR!! Invalid Directory")
        exit(2)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
