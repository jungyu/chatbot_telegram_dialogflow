class Stock(object):
    def __init__(self, req):
        self.type = req.get("queryResult").get("parameters").get("serviceterm")
        self.chat_id = req.get("user").get("chat").get("id")
    
    def dayTrend(self, req, bot):
        self.chat_id = req.get("user").get("chat").get("id")
        #https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#working-with-files-and-media
        bot.sendPhoto(chat_id=self.chat_id, photo=open('images/fig1.png', 'rb'), caption='台積電 2330')
        speech = "台積電 2330"
        return { 
            "textToSpeech": speech,
            "ssml": speech,
            "displayText": speech
            }