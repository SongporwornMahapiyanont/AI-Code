from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

import requests
import json

channel_secret = "xxx"
channel_access_token = "xxx"

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except:
        pass
    
    return "Hello Line Chatbot"

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)
    
    if text == "โควิด":
        url=requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
        covid_obj=json.loads(url.content.decode("utf-8"))[0]
        date = covid_obj['update_date']
        new_case = covid_obj['new_case']
        text_out = "ข้อมูลโควิด ณ วันที่ " + date + " จำนวนผู้ติดเชื้อ " + str(new_case) + " คน"
        print(text_out)
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

if __name__ == "__main__":          
    app.run()

