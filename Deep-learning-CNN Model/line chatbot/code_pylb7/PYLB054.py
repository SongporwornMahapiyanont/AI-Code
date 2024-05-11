from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            VideoMessage)
import os
import tempfile
import openai

openai.api_key = "xxx"

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

@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    static_tmp_path = os.path.join(os.path.dirname(__file__),
                                   'static', 'tmp').replace("\\","/")
    print(static_tmp_path)
    # mp4-xclkjfla --> mp4-xclkjfla.mp4
    with tempfile.NamedTemporaryFile(dir=static_tmp_path,
                                     prefix='mp4' + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name # ไฟล์ภาพที่บันทึก จะมีแต่ชื่อไฟล์ ชื่อว่า mp4-xxxxxx ยังไม่มีนามสกุล

    dist_path = tempfile_path + '.mp4'    # เติมนามสกุลเข้าไปในชื่อไฟล์เป็น mp4-xxxxxx.mp4
    os.rename(tempfile_path, dist_path)   # เปลี่ยนชื่อไฟล์ภาพเดิมที่ยังไม่มีนามสกุลให้เป็น mp4-xxxxxx.mp4
    filename_fullpath = dist_path.replace("\\","/")
    print(filename_fullpath)

    video_file = open(filename_fullpath, "rb")

    transcript = openai.Audio.transcribe("whisper-1", video_file)
    print(transcript.text)
    
    text_out = "ประมวลผลเรียบร้อยแล้ว ได้ข้อความดังนี้"
    line_bot_api.reply_message(event.reply_token,
                               [TextSendMessage(text=text_out),
                                TextSendMessage(text=transcript.text)])

if __name__ == "__main__":          
    app.run()

