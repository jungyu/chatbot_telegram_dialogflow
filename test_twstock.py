#pip install -U kaleido
import os

import requests

import numpy as np
import plotly.graph_objects as go


#個股日成交資訊
#https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html
#以 2330 台積電 為例，以下可以直接取得 JSON 內容
#https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210524&stockNo=2330
url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'
params = dict(
    response='json',
    date='20210524',
    stockNo='2330'
)

res = requests.get(url=url, params=params)
jsonData = res.json()
print(jsonData.get('fields'))
#print(data.get('data'))
#print(type(jsonData.get('data')))
#轉換 list 變 numpy 陣列
nData = np.array(jsonData.get('data'))
'''
print(jsonData.get('fields')[3])
print(nData[:,3]) #取每列的第3欄

print(jsonData.get('fields')[4])
print(nData[:,4]) #取每列的第4欄

print(jsonData.get('fields')[5])
print(nData[:,5]) #取每列的第5欄

print(jsonData.get('fields')[6])
print(nData[:,6]) #取每列的第6欄
'''
#參考： https://plotly.com/python/candlestick-charts/
#https://plotly.com/python/static-image-export/

fig = go.Figure(data=[go.Candlestick(x=nData[:,0],
                open=nData[:,3],
                high=nData[:,4],
                low=nData[:,5],
                close=nData[:,6])])

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/fig1.png")

'''
Web Visualization with Plotly and Flask.
https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
'''