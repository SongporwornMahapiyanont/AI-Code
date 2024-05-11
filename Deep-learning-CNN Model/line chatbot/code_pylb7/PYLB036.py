from flask import Flask, request, send_from_directory
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)
import os

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
    
    text_file = os.getcwd() + '/text/text_log.txt'
    text_file = text_file.replace("\\","/")
    print(text_file)
   
    try:
        file_obj = open(text_file, 'a') # r   w   a
        file_obj.write('\n' + text + '\n')
        file_obj.close()
    except IOError:
        print("File not found or path is incorrect")
    
    text_out = "บันทึกข้อความเรียบร้อย"
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))
    
@app.route('/text/<path:path>')
def send_text_content(path):
    return send_from_directory('text', path)

if __name__ == "__main__":          
    app.run()

