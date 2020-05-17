import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

import matplotlib.pyplot as plt
#from winsound import *
from PIL import ImageTk,Image 

import pygame


def analysis(span):
    pygame.init()
    
    b=float(span.text)
    to_append = [b]
    df_length = len(df)
    df.loc[df_length] = to_append
    plotgraph(df)

    '''
    if b>a: #New Price is higher than the Previous Price
        
        pygame.mixer.music.load('Sad.mp3')
        pygame.mixer.music.play(0)
    else:
     
        pygame.mixer.music.load('Sad.mp3')
        pygame.mixer.music.play(0)
    '''
    a=b
    
    if a==64.10:
    
        pygame.mixer.music.load('Ta_da.mp3')
        pygame.mixer.music.play(0)
        

    
def plotgraph(df):

    plt.plot(df.index,df.Price)
    plt.show()





def extract_data(soup):
    results = soup.find("div", {"data-field" : "Mid"})
    span=results.find("span", {"class" : "push-data aktien-big-font text-nowrap no-padding-at-all"})
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
    final_lst=[]

    while True:    
        url()
        time.sleep(10)
    
    