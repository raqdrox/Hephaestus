import random
import string
import time
import sys
import requests
from bs4 import BeautifulSoup

WebsiteString="https://prnt.sc/"

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

def getwebsite():
    pagestr=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    return WebsiteString+pagestr


def loop(amt , prefix):
    i=0
    while i<amt:
        webs=getwebsite()
        print('Trying : '+webs)
        html = requests.get(webs,headers=headers)
        
        soup = BeautifulSoup(html.content,features="html5lib")
        img_src = soup.find('img')
        
        #time.sleep(1) #uncomment to add delay
        
        if img_src!=None:
            if img_src['src'].startswith("//"):
                continue
            response = requests.get(img_src['src'],headers=headers)
            print(response.reason)
            if response.status_code == 200:
                i+=1
                with open(f"./results/{prefix}{i}.jpg", 'wb') as f:
                    f.write(response.content)
            

def cli_main(args):
    if type(args[1]) != int or type(args[2]) != str:
        print("Invalid Arguments")
        print("Format: Scraper.py <number of results> <filename prefix>")
        return 0
    loop(args[0],args[1])
    return 1


def main():
    print("Screenshot Scraper by Raqdrox")
    resamt= int(input("Number Of Results : "))
    imgpre= input("Filename Prefix : ")
    loop(resamt,imgpre)
    print("Finished!!!")
    return 1

if __name__=="__main__":
    if len(sys.argv)==3:
        cli_main(sys.argv)
    else:
        main()