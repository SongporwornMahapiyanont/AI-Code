from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

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
                    text_out = "สวัสดี ยินดีที่ได้รู้จักนะ"
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))
                       
                if (intents_name=="weather"):
                    text_out = "อากาศเย็นสบาย"
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))               
                    
                if (intents_name=="date"):
                    text_out = "วันนี้วันพระ"
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))

                if (intents_name=="joke"):
                    text_out = "เราจะพาไปกินอาหารญี่ปุ่นนะ เมนูนี้ชื่อว่า ข้าวคลิกกะปุ"
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))
                    
            else:
                print("intent = unknow")
        else:
            print("intent = unknow")
            
if __name__ == "__main__":          
    app.run()

