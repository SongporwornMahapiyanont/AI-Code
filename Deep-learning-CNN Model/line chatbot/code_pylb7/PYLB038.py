from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            ImageMessage)
import os
import tempfile

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

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    static_tmp_path = os.path.join(os.path.dirname(__file__),
                                   'static', 'tmp').replace("\\","/")
    print(static_tmp_path)
    # jpg-xclkjfla --> jpg-xclkjfla.jpg
    with tempfile.NamedTemporaryFile(dir=static_tmp_path,
                                     prefix='jpg' + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name # ไฟล์ภาพที่บันทึก จะมีแต่ชื่อไฟล์ ชื่อว่า jpg-xxxxxx ยังไม่มีนามสกุล

    dist_path = tempfile_path + '.jpg'    # เติมนามสกุลเข้าไปในชื่อไฟล์เป็น jpg-xxxxxx.jpg
    os.rename(tempfile_path, dist_path)   # เปลี่ยนชื่อไฟล์ภาพเดิมที่ยังไม่มีนามสกุลให้เป็น jpg-xxxxxx.jpg
    
    text_out = "บันทึกรูปภาพเรียบร้อย"
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))

if __name__ == "__main__":          
    app.run()

