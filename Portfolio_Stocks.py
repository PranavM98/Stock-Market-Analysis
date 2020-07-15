import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import datetime
import matplotlib.pyplot as plt
#from winsound import *
from PIL import ImageTk,Image 
import csv
import pygame
from gtts import gTTS 
import os


def texttoaudio(text):
    myobj = gTTS(text=text, lang='en', slow=False) 
    myobj.save("text.mp3") 
    pygame.mixer.music.load('text.mp3')
    pygame.mixer.music.play(0)
    os.remove("text.mp3") #remove file from system
    time.sleep(8)


def analysis(data):
    
    
    pygame.init()
    

    length=len(data)
    #Partitioning into 3 sub tables
    
    BMS=data['Price-BMS']
    GS=data['Price-GS']
    AMAZON=data['Price-Amazon']
    if length>1:

        #BMS
        
        count=0
        for i in (BMS,GS,AMAZON):
            
            if count==0:
                company='B M S'
            elif count==1:
                company='Goldman Sachs'
            else:
                company='Amazon'
            
        
            new=i[length-1]
            previous=i[length-2]
            
            #Sometimes if the price is 4 digits (6,243.53), remove the comma
 
            
            new=float(new)
            previous=float(previous)
            print("PREVIOUS: ",previous)
            print("NEW: ",new)

                
            change_percentage=round(float((new-previous)/previous)*100,2)
         
    
            if new>previous: #New price higher than previous price
                pygame.mixer.music.load('Ta_da.mp3')
                pygame.mixer.music.play(0)
                text= company +" Stock Price went up by "+str(change_percentage)+" percent"
                texttoaudio(text)
                
          
              
                
            elif new<previous:
                
                     
                #pygame.mixer.music.load('Sad.mp3')
                #pygame.mixer.music.play(0)
                
                text=company+" Stock Price went down by "+str(change_percentage)+" percent"
                texttoaudio(text)
    
    
            else:
                print("No Change")
                #text=company +" stock price has not changed."
                #texttoaudio(text)
            
            count=count+1
        

    plotgraph(data)
    
def plotgraph(data):

    #fig, axs = plt.subplots(3,1,constrained_layout=True)

    plt.plot(data['Price-BMS'], color='r', label='BMS')
    plt.title('Bristol Myers Squibb',fontname="Times New Roman Bold")
    #axs[0].set_xlabel('Time')
    plt.ylabel('Price')
    plt.show()
    
    plt.plot(data['Price-GS'],color='g', label='GS')
    plt.title('Goldman Sachs',fontname="Times New Roman Bold")
    #axs[1].set_xlabel('Time')
    plt.ylabel('Price')
    plt.show()
    
    plt.plot(data['Price-Amazon'],color='b', label='AMAZON')
    plt.title('Amazon', fontname="Times New Roman Bold")
    #axs[2].set_xlabel('Time')
    plt.ylabel('Price')

    plt.show()





def extract_data(soup_list):
    result_list=[]
    for soup in soup_list:
        results = soup.find("div", {"data-field" : "Mid"})
        span=results.find("span", {"class" : "push-data aktien-big-font text-nowrap no-padding-at-all"})
        price=span.text
        print(price)
        if price.find(',')!=-1:
            print(price)
            res=float(price.replace(',',''))
            #res=float(res)
            print("NEW:",res)
            result_list.append(float(res))
        else:
            result_list.append(float(span.text))
    
    result_list.append(time.ctime())
    #print(result_list)
        #break
    df.loc[len(df)] = result_list
    #df.index=df["Time"]

 
    analysis(df)
    


def url():
    url='https://markets.businessinsider.com/stocks/bmy-stock'
    url1='https://markets.businessinsider.com/stocks/gs-stock'
    url2='https://markets.businessinsider.com/stocks/amzn-stock'
    
    
    html=urlopen(url)
    soup= BeautifulSoup(html,'lxml')

    html1=urlopen(url1)
    soup1= BeautifulSoup(html1,'lxml')

    html2=urlopen(url2)
    soup2= BeautifulSoup(html2,'lxml')

    soup_list=[soup,soup1,soup2]

    
    extract_data(soup_list)






if __name__ == "__main__":
    df=pd.DataFrame(columns=["Price-BMS","Price-GS","Price-Amazon","Time"])
    count=0
    final_lst=[]
    url()

    while True:
        url()
        time.sleep(30)
        print("")
