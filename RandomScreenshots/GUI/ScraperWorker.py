from bs4 import BeautifulSoup
import random
import string
import time
import requests
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal,pyqtSlot)

class ScraperThread(QObject):

    _amount=0
    _prefix='image'
    WebsiteString="https://prnt.sc/"
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }

    def __init__(self, amt,pref, parent=None):
        QObject.__init__(self, parent)
        self._amount=amt
        self._prefix=pref




    def getwebsite(self):
        pagestr=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        return self.WebsiteString+pagestr
    

    finished= pyqtSignal()
    progress= pyqtSignal(int)
    currprog=0
    running=True

    def loop(self):
        print(self._amount)
        i=0
        while i<self._amount and self.running:
            webs=self.getwebsite()
            print('Trying : '+webs)
            html = requests.get(webs,headers=self.headers)
            
            soup = BeautifulSoup(html.content,features="html5lib")
            img_src = soup.find('img')
            
            #time.sleep(1) #uncomment to add delay
            
            if img_src!=None:
                if img_src['src'].startswith("//"):
                    continue
                response = requests.get(img_src['src'],headers=self.headers)
                print(response.reason)
                if response.status_code == 200:
                    i+=1
                    self.currprog+=100/self._amount
                    self.progress.emit(self.currprog)
                    with open(f"./results/{self._prefix}{i}.jpg", 'wb') as f:
                        f.write(response.content)
        self.finished.emit()

    def stop(self):
        self.running=False

