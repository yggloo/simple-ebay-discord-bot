import requests
import threading
import time

def views(link,num_views):
    #send views requests to the link using threading
    for i in range(num_views):
        threading.Thread(target=requests.get, args=(link,)).start()
        time.sleep(.1)
        print(f'{i+1} views sent')

