import json
import os

from flask import Flask
from flask import request
from flask import make_response

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

def makeWebhookResult(req):
    #askweather的地方是Dialogflow>Intent>Action 取名的內容
    if req.get("queryResult").get("action") != "askweather":
        return {}
    result = req.get("queryResult")
    parameters = result.get("parameters")
    #parameters.get("weatherlocation")的weatherlocation是Dialogflow > Entitiy
    #也就是步驟josn格式中parameters>weatherlocation
    zone = parameters.get("weatherlocation")

    with open('taiwan_districts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    z = Zone(data, zone)
    fullZone = z.getFullZone()

    w = Weather(fullZone)
    #speech就是回應的內容
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

if __name__ == "__main__":
    app.run()