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
        # กำหนดได้แค่ 2 ทางเลือก เช่น Yes No หรือ ร้อน เย็น เป็นต้น
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='ร้อน', text='กาแฟร้อน'),
            MessageAction(label='เย็น', text='กาแฟเย็น')])
        
        template_message = TemplateSendMessage(alt_text="Hello",
                                               template=confirm_template)
        line_bot_api.reply_message(event.reply_token,template_message)

    if text == 'กาแฟร้อน':
        ask_text = 'คุณต้องการรับ size ใด'        
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='แก้วเล็ก', text='คุณสั่งกาแฟร้อนแก้วเล็ก'),
            MessageAction(label='แก้วใหญ่', text='คุณสั่งกาแฟร้อนแก้วใหญ่')])
        
        template_message = TemplateSendMessage(alt_text="Hello",
                                               template=confirm_template)
        line_bot_api.reply_message(event.reply_token,template_message)

    if text == 'กาแฟเย็น':
        ask_text = 'คุณต้องการความหวานแบบใด'
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='หวานปกติ', text='คุณสั่งกาแฟเย็นหวานปกติ'),
            MessageAction(label='หวานน้อย', text='คุณสั่งกาแฟเย็นหวานน้อย')])
        
        template_message = TemplateSendMessage(alt_text="Hello",
                                               template=confirm_template)
        line_bot_api.reply_message(event.reply_token,template_message)

if __name__ == "__main__":          
    app.run()

