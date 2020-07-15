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



def texttoaudio(text):
    myobj = gTTS(text=text, lang='en', slow=False) 
    myobj.save("text.mp3") 
    pygame.mixer.music.load('text.mp3')
    pygame.mixer.music.play(0)
    os.remove("text.mp3") #remove file from system


def analysis(data):
    
    
    pygame.init()
    

    length=len(data)
    #Partitioning into 3 sub tables
    
    BMS=data['Price-BMS']
    GS=data['Price-GS']
    AMAZON=data['Price-Amazon']
    if len(data)>1:

        #BMS
    
        if BMS[length-1]>BMS[length-2]: #New price higher than previous price
            pygame.mixer.music.load('Ta_da.mp3')
            pygame.mixer.music.play(0)
            change_percentage=float((BMS[length-1]-BMS[length-2])/BMS[length-2])*100
            text="B M S Stock Price went up by "+str(change_percentage)+" percent"
            texttoaudio(text)
            
      
          
            
        elif BMS[length-1]<BMS[length-2]:
            
                 
            pygame.mixer.music.load('Sad.mp3')
            pygame.mixer.music.play(0)
            
            change_percentage=float(abs(BMS[length-1]-BMS[length-2])/BMS[length-2])*100
            text="B M S Stock Price went down by "+str(change_percentage)+" percent"
            texttoaudio(text)


        else:
            print("No Change")
            change_percentage=float(abs(BMS[length-1]-BMS[length-2])/BMS[length-2])*100
            text="B M S stock price has not changed."
            texttoaudio(text)
            
    
        #Goldman Sachs
        if GS[length-1]>GS[length-2]: #New price higher than previous price
            pygame.mixer.music.load('Ta_da.mp3')
            pygame.mixer.music.play(0)
            change_percentage=float((GS[length-1]-GS[length-2])/GS[length-2])*100
            text="Goldman Sachs Stock Price went up by "+str(change_percentage)+" percent"
            texttoaudio(text)
            
      
          
            
        elif GS[length-1]<GS[length-2]:
            
                 
            pygame.mixer.music.load('Sad.mp3')
            pygame.mixer.music.play(0)
            
            change_percentage=float(abs(GS[length-1]-GS[length-2])/GS[length-2])*100
            text="Goldman Sachs Stock Price went down by "+str(change_percentage)+" percent"
            texttoaudio(text)


        else:
            print("No Change")
            change_percentage=float(abs(GS[length-1]-GS[length-2])/GS[length-2])*100
            text="Goldman Sachs stock price has not changed."
            texttoaudio(text)
            

        #Amazon
        
        if AMAZON[length-1]>AMAZON[length-2]: #New price higher than previous price
            pygame.mixer.music.load('Ta_da.mp3')
            pygame.mixer.music.play(0)
            change_percentage=float((AMAZON[length-1]-AMAZON[length-2])/AMAZON[length-2])*100
            text="AMAZON Stock Price went up by "+str(change_percentage)+" percent"
            texttoaudio(text)
            
      
          
            
        elif AMAZ0N[length-1]<AMAZON[length-2]:
            
                 
            pygame.mixer.music.load('Sad.mp3')
            pygame.mixer.music.play(0)
            
            change_percentage=float(abs(AMAZON[length-1]-AMAZON[length-2])/AMAZON[length-2])*100
            text="Amazon Stock Price went down by "+str(change_percentage)+" percent"
            texttoaudio(text)


        else:
            print("No Change")
            change_percentage=float(abs(AMAZON[length-1]-AMAZON[length-2])/AMAZON[length-2])*100
            text="AMAZON stock price has not changed."
            texttoaudio(text)
            


    plotgraph(data)
    
def plotgraph(data):

    fig, axs = plt.subplots(3,1,constrained_layout=True)
    
    axs[0].plot(data.index,data['Price-BMS'], color='r', label='BMS')
    axs[0].set_title('Bristol Myers Squibb',fontname="Times New Roman Bold")
    #axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Price')
    
    
    axs[1].plot(data.index, data['Price-GS'],color='g', label='GS')
    axs[1].set_title('Goldman Sachs',fontname="Times New Roman Bold")
    #axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Price')
    
    
    axs[2].plot(data.index,data['Price-Amazon'],color='b', label='AMAZON')
    axs[2].set_title('Amazon', fontname="Times New Roman Bold")
    #axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Price')



    plt.show()





def extract_data(soup_list):
    result_list=[]
    for soup in soup_list:
        results = soup.find("div", {"data-field" : "Mid"})
        span=results.find("span", {"class" : "push-data aktien-big-font text-nowrap no-padding-at-all"})
        result_list.append(span.text)
    
    result_list.append(time.ctime())
    #print(result_list)
        #break
    df.loc[len(df)] = result_list
    df.index=df["Time"]
    data=df.drop(columns="Time",axis=0)
    print(data)
    
    


    analysis(data)
    


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
