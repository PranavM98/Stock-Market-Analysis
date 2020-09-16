import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import datetime
import matplotlib.pyplot as plt
#from winsound import *
from gtts import gTTS 
from PIL import ImageTk,Image 
import csv
import pygame
import os 


def analysis(span):
    pygame.init()
    
    
    
    price=float(span.text)
    final_lst.append(price)
    
    length=len(final_lst)
    
    
    if length!=1:
        
    
        if final_lst[length-1]>final_lst[length-2]: #New Price is higher than the Previous Price
            
            pygame.mixer.music.load('Ta_da.mp3')
            pygame.mixer.music.play(0)
            
            change_percentage=float((final_lst[length-1]-final_lst[length-2])/final_lst[length-2])*100
            
            text="B M S Stock Price went up by "+str(change_percentage)+" percent"
            print(text)
            myobj = gTTS(text=text, lang='en', slow=False) 
            myobj.save("text.mp3") 
            pygame.mixer.music.load('text.mp3')
            pygame.mixer.music.play(0)

        
        elif final_lst[length-1]<final_lst[length-2]: # New price is lower than previous price
     
            pygame.mixer.music.load('Sad.mp3')
            pygame.mixer.music.play(0)
            
            change_percentage=float(abs(final_lst[length-1]-final_lst[length-2])/final_lst[length-2])*100
            text="B M S Stock Price went down by "+str(change_percentage)+" percent"
            print(text)
            myobj = gTTS(text=text, lang='en', slow=False) 
            myobj.save("text.mp3") 
            pygame.mixer.music.load('text.mp3')
            pygame.mixer.music.play(0)

            
        
        else:
            
            print("No Change")
            change_percentage=float(abs(final_lst[length-1]-final_lst[length-2])/final_lst[length-2])*100
            text="B M S stock price has not changed."
            
            myobj = gTTS(text=text, lang='en', slow=False) 
            myobj.save("text.mp3") 
            pygame.mixer.music.load('text.mp3')
            pygame.mixer.music.play(0)
            os.remove("text.mp3") #remove the file from the system
            

            
    
    
    
    df.loc[len(df)] = [price]
    plotgraph(df)
    
def plotgraph(df):

    plt.plot(df.index,df.Price)
    plt.show()





def extract_data(soup):
    results = soup.find("div", {"class" : "price-section__values"})
    span=results.find("span", {"class" : "price-section__current-value"})
    print(span.text, end=' ')
    print(time.ctime())
    analysis(span)
    


def url():
    url='https://markets.businessinsider.com/stocks/bmy-stock'
    html=urlopen(url)
    soup= BeautifulSoup(html,'lxml')

    extract_data(soup)






if __name__ == "__main__":
    df=pd.DataFrame(columns=["Price"])
    count=0
    final_lst=[]
    while True:
        now = datetime.datetime.now()
        seven_pm = now.replace(hour=19, minute=0, second=0, microsecond=0)
        one_am=now.replace(hour=1,minute=30,second=0,microsecond=0)
        
        #print("NOW:",now)
        #print("7 PM:",seven_pm)
        #print("1:30 AM:",one_am)
        
        #while now>seven_pm and now<one_am:    
        url()
        time.sleep(30)
        print("")
    count=count+1
        
        
        