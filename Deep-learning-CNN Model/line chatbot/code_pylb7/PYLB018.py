from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            StickerSendMessage)

import random

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

play_status = False
number = 0

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    global play_status,number
    text = event.message.text
    print(text)

    if (play_status == False):
        if text == "ขอเล่นเกม":
            number = random.randint(0,99) # 18
            #print(number)
            text_out = "เริ่มทายตัวเลข 0 ถึง 99 ได้เลยครับ"
            print(text_out)
            line_bot_api.reply_message(event.reply_token,
                                       TextSendMessage(text=text_out))
            play_status = True
            
    if (play_status == True): 
        num = int(text) # "50" --> 50
        if (num == number): #num ผู้เล่นพิมพ์เข้ามา , number เลขโจทย์
          #  50 == 18
            text_out = "ถูกต้องนะครับ เก่งจริงๆ"
            print(text_out)
            p_id = 11537 
            s_id = 52002734 
            line_bot_api.reply_message(event.reply_token,
                                       [TextSendMessage(text=text_out),
                                        StickerSendMessage(package_id=p_id,
                                                           sticker_id=s_id)])
            play_status = False
            
        else: #ตอบผิด
            if (num > number): # 50 > 18
                text_out = "มากไปนะครับ"
                print(text_out)
                line_bot_api.reply_message(event.reply_token,
                                           TextSendMessage(text=text_out))
            else:              
                text_out = "น้อยไปนะครับ"
                print(text_out)
                line_bot_api.reply_message(event.reply_token,
                                           TextSendMessage(text=text_out))

if __name__ == "__main__":          
    app.run()
