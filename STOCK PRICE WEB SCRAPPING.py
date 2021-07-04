#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import requests
from bs4 import BeautifulSoup


# In[18]:


def Stock_Code_Data(code):
    stockcode = code
    stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stockcode)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    for item in data_array:
        if 'basePrice"' in item:
            index = data_array.index(item)+1
            basePrice=data_array[index].split('"')[1]
        if  'dayHigh"' in item:
            index = data_array.index(item)+1
            dayHigh=data_array[index].split('"')[1]
        if  'averagePrice"' in item:
            index = data_array.index(item)+1
            averagePrice=data_array[index].split('"')[1]
        if  'previousClose"' in item:    
            index = data_array.index(item)+1
            previousClose=data_array[index].split('"')[1]
        if  'dayLow"' in item:
            index = data_array.index(item)+1
            dayLow=data_array[index].split('"')[1]
        if  'open"' in item:
            index = data_array.index(item)+1
            openval=data_array[index].split('"')[1]
        if  'closePrice"' in item:
            index = data_array.index(item)+1
            closePrice=data_array[index].split('"')[1]
        if  'lastPrice"' in item:
            index = data_array.index(item)+1
            lastPrice=data_array[index].split('"')[1]
    return(basePrice,dayHigh,averagePrice,previousClose,dayLow,openval,closePrice,lastPrice)      


# In[27]:


import time
from datetime import datetime
df = pd.DataFrame(columns=['DateTime', 'BasePrice', 'DayHigh','AveragePrice','previousClose','DayLow','ClosePrice','LastPrice'])
while True:
    time.sleep(60)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    base_price,day_High,average_Price,previous_Close,day_Low,open_val,close_Price,last_Price=Stock_Code_Data('TATAELXSI')
    df = df.append({'DateTime':dt_string,'BasePrice': base_price, 'DayHigh': day_High, 'AveragePrice': average_Price,'previousClose':previous_Close,'DayLow':day_Low,'ClosePrice':close_Price,'LastPrice':last_Price}, ignore_index=True)
    print(df)
    print('*'*50)
        


# In[ ]:




