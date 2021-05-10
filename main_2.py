'''
Tutorial_2:
‧為了加入更多的 action 判斷，重構了程式：匯入 util 裡的 Switch (Python 3.10 之後才有 Match case) ，進行函式判斷切換
'''
import json
import os

from flask import Flask
from flask import request
from flask import make_response

from util import Switch
from weather import Zone, Weather

app = Flask(__name__)
#run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/", methods=['GET'])
def hello():
    return '您好，我是 vegetabot，很高興為您服務'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def askServices(req):
    return None

def askWeather(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    zone = parameters.get("weatherlocation")

    with open('taiwan_districts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    z = Zone(data, zone)
    fullZone = z.getFullZone()

    w = Weather(fullZone)
    speech = '您所查詢的：{}，目前的氣象如下：{}'.format(fullZone, w.yamWeather())
    print("Response:")
    print(speech)
    #回傳
    return { 
      "textToSpeech": speech,
      "ssml": speech,
      "fulfillmentText": speech,
      "displayText": speech
    }

def askNews(req):
    return None

def askOilPrice(req):
    return None

def askPrice(req):
    return None


def doAction(req):
    response = None
    for case in Switch(req.get("queryResult").get("action")):

        if case('askServices'):
            print('詢問服務項目')
            response = askServices(req)
            break
        if case('askWeather'):
            print('詢問氣象')
            response = askWeather(req)
            break
        if case('askNews'):
            print('詢問新聞')
            response = askNews(req)
            break
        if case('askOilPrice'):
            print('詢問油價')
            response = askOilPrice(req)
            break
        if case('askPrice'):
            print('詢問某商品價格')
            response = askPrice(req)
            break
        if case():
            print('無對應動作')

    return response

def makeWebhookResult(req):
    response = doAction(req)
    if response == None:
        return {}
    
    print("Response:")
    print(response)
    #回傳
    return response

if __name__ == "__main__":
    app.run()