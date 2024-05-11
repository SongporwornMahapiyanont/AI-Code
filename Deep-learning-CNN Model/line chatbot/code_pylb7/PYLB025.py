from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TemplateSendMessage,
                            ConfirmTemplate,
                            MessageAction)

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
    
    if text == 'กาแฟ':
        ask_text = 'คุณต้องการดื่มกาแฟแบบใด'
        # กำหนดได้ไม่เกิน 2 ตัวเลือก เช่น Yes No หรือ ร้อน เย็น เป็นต้น
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='ร้อน', text='ขอสั่งกาแฟร้อน'),
            MessageAction(label='เย็น', text='ขอสั่งกาแฟเย็น')])
        
        template_message = TemplateSendMessage(alt_text="Hello",
                                               template=confirm_template)

        line_bot_api.reply_message(event.reply_token,template_message)
            
if __name__ == "__main__":          
    app.run()

