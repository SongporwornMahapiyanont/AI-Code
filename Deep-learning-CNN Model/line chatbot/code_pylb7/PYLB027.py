from flask import Flask, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TemplateSendMessage,
                            MessageAction,
                            ButtonsTemplate,
                            ConfirmTemplate,
                            URIAction)

channel_secret = "xxx"
channel_access_token = "xxx"

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
      
    if text == 'กาแฟ':
        text_show = 'คุณต้องการดื่มกาแฟแบบใด'
        #img_url = request.url_root + '/static/cafe.jpg'
        img_url = 'https://cdn.pixabay.com/photo/2019/11/11/15/32/coffee-4618705_960_720.jpg'

        # กำหนดได้ไม่เกิน 4 ตัวเลือก
        buttons_template = ButtonsTemplate(
            title='เข้มข้น Cafe ยินดีให้บริการ', text=text_show,
            thumbnail_image_url = img_url,actions=[
                MessageAction(label='ร้อน', text='คุณสั่งกาแฟร้อน'),
                MessageAction(label='เย็น', text='คุณสั่งกาแฟเย็น'),
                MessageAction(label='ปั่น', text='คุณสั่งกาแฟปั่น'),
                URIAction(label='เข้าดูเว็บไซต์',uri='https://ee-eng.su.ac.th')])

        template_message = TemplateSendMessage(alt_text='Hello',
                                               template=buttons_template)
        line_bot_api.reply_message(event.reply_token,template_message)

    if text == 'คุณสั่งกาแฟร้อน':
        ask_text = 'คุณต้องการรับ size ใด'        
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='แก้วเล็ก', text='คุณสั่งกาแฟร้อนแก้วเล็ก'),
            MessageAction(label='แก้วใหญ่', text='คุณสั่งกาแฟร้อนแก้วใหญ่')])
        
        template_message = TemplateSendMessage(alt_text=ask_text,
                                               template=confirm_template)
        line_bot_api.reply_message(event.reply_token,template_message)

@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)
            
if __name__ == "__main__":          
    app.run()

