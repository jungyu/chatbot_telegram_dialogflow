import os

import requests

import numpy as np
import plotly.graph_objects as go

class Stock(object):
    def __init__(self, req):
        self.type = req.get("queryResult").get("parameters").get("serviceterm")
        self.chat_id = req.get("user").get("chat").get("id")
    
    #個股日成交資訊
    #https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html
    def dayTrend(self, req, bot):
        self.chat_id = req.get("user").get("chat").get("id")

        url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'
        params = dict(
            response='json',
            date='20210525',
            stockNo='2330'
        )
        res = requests.get(url=url, params=params)
        jsonData = res.json()
        #轉換 list 變 numpy 陣列
        nData = np.array(jsonData.get('data'))

        fig = go.Figure(data=[go.Candlestick(x=nData[:,0],
            open=nData[:,3],
            high=nData[:,4],
            low=nData[:,5],
            close=nData[:,6])])

        if not os.path.exists("images"):
            os.mkdir("images")

        fig.write_image("images/dayTrend.png")

        #https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#working-with-files-and-media
        bot.sendPhoto(chat_id=self.chat_id, photo=open('images/dayTrend.png', 'rb'), caption='台積電 2330')
        speech = "台積電 2330"
        return { 
            "textToSpeech": speech,
            "ssml": speech,
            "displayText": speech
            }