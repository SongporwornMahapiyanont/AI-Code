from flask import Flask, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            StickerSendMessage,
                            ImageSendMessage)

import openai
import requests
from io import BytesIO
from PIL import Image
import os
import GT

channel_secret = "xxx"
channel_access_token = "xxx"

openai.api_key = "xxx"

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

    prompt_text_th = text
    prompt_text_en = GT.translate(prompt_text_th,'th','en') # th --> en
    print(prompt_text_th)
    print(prompt_text_en)

    response = openai.Image.create(
        prompt = prompt_text_en,
        n = 1, # ต้องการภาพ output กี่แบบ
        size = "512x512") # 256x256, 512x512, 1024x1024

    img_url = response['data'][0]['url']
    img_data = requests.get(img_url).content
    img = Image.open(BytesIO(img_data))
    static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp').replace("\\","/")
    filename_image = 'ai_image.jpg'
    img.save(static_tmp_path+'/'+filename_image) #บันทึกภาพลงห้อง tmp
                  
    img_url = request.host_url + os.path.join('static', 'tmp', filename_image).replace("\\","/")
    print(img_url)
    line_bot_api.reply_message(
        event.reply_token,[
            TextSendMessage(text='สร้างภาพเสร็จเรียบร้อยแล้ว'),
            ImageSendMessage(img_url,img_url)])
                               
@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)
            
if __name__ == "__main__":          
    app.run()

