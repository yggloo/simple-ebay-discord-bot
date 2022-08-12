import requests
import threading
import time

def views(link,views):
    #send views requests to the link using threading
    for i in range(views):
        threading.Thread(target=requests.get, args=(link,)).start()
        time.sleep(.1)
        print(f'{i+1} views sent')

