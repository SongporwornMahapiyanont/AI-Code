from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

import random
from wit import Wit

channel_secret = "xxx"
channel_access_token = "xxx"

wit_access_token = "xxx"
client = Wit(wit_access_token)

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

answer_greeting = ["ยินดีที่ได้รู้จัก","ดีครับ","หวัดดีเพื่อนใหม่"]
answer_weather = ["ร้อนมาก","ร้อนที่สุด","ร้อนหน้าไหม้","ร้อนจริงๆ"]
answer_date = ["วันนี้วันพระ","วันหยุดราชการ","วันสงกรานต์","วันขึ้นปีใหม่"]
answer_joke = ["รองเท้าอะไรหายากที่สุด.... รองเท้าหาย","ทอดหมูยังไงไม่ให้ติดกระทะ.... ใช้หม้อทอด"]

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)
    
    if (text != ""):
        ret = client.message(text)
        if len(ret["intents"]) > 0:
            confidence = ret["intents"][0]['confidence']
            
            if (confidence > 0.8):
                intents_name = ret["intents"][0]['name']        
                print("intent = ",intents_name)

                if (intents_name=="greeting"):
                    idx = random.randint(0,len(answer_greeting)-1)
                    text_out = answer_greeting[idx]
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))
                   
                if (intents_name=="weather"):
                    idx = random.randint(0,len(answer_weather)-1)
                    text_out = answer_weather[idx]
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))               
                    
                if (intents_name=="date"):
                    idx = random.randint(0,len(answer_date)-1)
                    text_out = answer_date[idx]
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))
                    
                if (intents_name=="joke"):
                    idx = random.randint(0,len(answer_joke)-1)
                    text_out = answer_joke[idx]
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))
                    
            else:
                print("intent = unknow")
                text_out = "ฉันไม่เข้าใจสิ่งที่คุณถาม กรุณาถามใหม่อีกครั้ง"
                line_bot_api.reply_message(event.reply_token,
                                           TextSendMessage(text=text_out))
        else:
            print("intent = unknow")
            text_out = "ฉันไม่เข้าใจสิ่งที่คุณถาม กรุณาถามใหม่อีกครั้ง"
            line_bot_api.reply_message(event.reply_token,
                                       TextSendMessage(text=text_out))
            
if __name__ == "__main__":          
    app.run()

