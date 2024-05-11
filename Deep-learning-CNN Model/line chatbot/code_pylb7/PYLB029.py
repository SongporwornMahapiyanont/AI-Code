from flask import Flask, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TemplateSendMessage,
                            MessageAction,
                            ImageCarouselTemplate,
                            ImageCarouselColumn,
                            ConfirmTemplate)

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
        
    if text == 'เค้ก':
        #img_url_1 = request.url_root + '/static/cake1.png'
        #img_url_2 = request.url_root + '/static/cake2.png'
        #img_url_3 = request.url_root + '/static/cake3.png'
        #img_url_4 = request.url_root + '/static/cake4.png'

        img_url_1 = 'https://cdn.pixabay.com/photo/2020/12/17/10/18/cheesecake-5838905_960_720.jpg'
        img_url_2 = 'https://cdn.pixabay.com/photo/2014/11/28/08/03/brownie-548591_960_720.jpg'
        img_url_3 = 'https://cdn.pixabay.com/photo/2018/03/20/21/46/food-3244824_960_720.jpg'
        img_url_4 = 'https://cdn.pixabay.com/photo/2019/04/02/17/07/tiramisu-4098241_960_720.jpg'

        # กำหนดได้ไม่เกิน 10 อัน
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url=img_url_1,action=
                MessageAction(label='รายละเอียด',text='ชีสเค้กมิกซ์เบอรี่ 120 บาท')),
            ImageCarouselColumn(image_url=img_url_2,action=
                MessageAction(label='รายละเอียด',text='บราวนี่ 80 บาท')),
            ImageCarouselColumn(image_url=img_url_3,action=
                MessageAction(label='รายละเอียด',text='เค้กมะม่วง 90 บาท')),
            ImageCarouselColumn(image_url=img_url_4,action=
                MessageAction(label='รายละเอียด',text='เค้กทีรามิสุ 135 บาท'))])
        
        template_message = TemplateSendMessage(alt_text='Hello',
                                               template=image_carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    if text == 'เค้กมะม่วง 90 บาท':
        ask_text = 'คุณต้องการรับกี่ชิ้น'
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='1 ชิ้น', text='คุณรับเค้ก 1 ชิ้น'),
            MessageAction(label='2 ชิ้น', text='คุณรับเค้ก 2 ชิ้น')])
        
        template_message = TemplateSendMessage(alt_text='Hello',
                                               template=confirm_template)
        line_bot_api.reply_message(event.reply_token,template_message)
 
@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)
            
if __name__ == "__main__":          
    app.run()

