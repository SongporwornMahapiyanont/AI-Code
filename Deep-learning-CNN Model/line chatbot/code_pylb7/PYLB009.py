from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            StickerSendMessage)

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
                    p_id = 446
                    s_id = 1989
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,
                                                                  sticker_id=s_id))
                   
                if (intents_name=="weather"):
                    p_id = 789
                    s_id = 10892
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,
                                                                  sticker_id=s_id))
                               
                if (intents_name=="date"):
                    p_id = 11537
                    s_id = 52002759
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,
                                                                  sticker_id=s_id))
                    
                if (intents_name=="joke"):
                    p_id = 11539
                    s_id = 52114116
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,
                                                                  sticker_id=s_id))
                    
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

