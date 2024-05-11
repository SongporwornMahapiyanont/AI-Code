from flask import Flask, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            StickerSendMessage,
                            ImageSendMessage)
from wit import Wit

channel_secret = "xxx"
channel_access_token = "xxx"

wit_access_token = "xxx"
client = Wit(wit_access_token)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)

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
                    text_out = "สวัสดีครับผม ยินดีที่ได้รู้จักครับ"
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text=text_out))
                   
                if (intents_name=="weather"):
                    url = request.url_root + '/static/beach.jpg'
                    #url = 'https://cdn.pixabay.com/photo/2017/01/20/00/30/maldives-1993704_960_720.jpg'
                    line_bot_api.reply_message(event.reply_token,
                                               ImageSendMessage(url,url))
                               
                if (intents_name=="date"):
                    url = request.url_root + '/static/happynewyear.png'
                    #url = 'https://cdn.pixabay.com/photo/2016/12/04/21/22/snowman-1882635_960_720.jpg'
                    line_bot_api.reply_message(event.reply_token,
                                               ImageSendMessage(url,url))
                    
                if (intents_name=="joke"):
                    p_id = 11538
                    s_id = 51626504
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,sticker_id=s_id))
                    
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

@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)
            
if __name__ == "__main__":          
    app.run()

