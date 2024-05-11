from flask import Flask, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            LocationSendMessage,
                            ImageSendMessage)

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
    
    if (text=="ประวัติภาควิชาวิศวกรรมไฟฟ้า"):
        text_out = "ภาควิชาวิศวกรรมไฟฟ้า คณะวิศวกรรมศาสตร์และเทคโนโลยีอุตสาหกรรม มหาวิทยาลัยศิลปากร ก่อตั้งและเปิดรับนักศึกษารุ่นแรกในปี พ.ศ. 2550"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

    if (text=="หลักสูตรที่เปิดสอน"):
        text_out = "ปัจจุบันภาควิชาวิศวกรรมไฟ้า เปิดสอนจำนวน 3 หลักสูตร ประกอบด้วย 1. ป.ตรี หลักสูตรวิศวกรรมศาสาตรบัณฑิต สาขาวิชาวิศวกรรมอิเล็กทรอนิกส์และระบบคอมพิวเตอร์ 2. ป.ตรี หลักสูตรวิศวกรรมศาสาตรบัณฑิต สาขาวิชาวิศวกรรมไฟฟ้าสื่อสาร และ 3. ป.โท หลักสูตรวิศวกรรมศาสตรมหาบัณฑิต สาขาวิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))
        
    if (text=="จำนวนนักศึกษา"):
        text_out = "ปัจจุบันภาควิชาวิศวกรรมไฟฟ้า มีจำนวนนักศึกษาระดับ ป.ตรี และ ป.โท รวมประมาณ 750 คน"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))
        
    if (text=="ภาพถ่ายการเรียนการสอน"):
        url1 = request.url_root + '/static/imgee1.jpg'
        url2 = request.url_root + '/static/imgee2.jpg'
        url3 = request.url_root + '/static/imgee3.jpg'
        line_bot_api.reply_message(event.reply_token,
                                   [ImageSendMessage(url1,url1),
                                    ImageSendMessage(url2,url2),
                                    ImageSendMessage(url3,url3)])
                
    if (text=="สถานที่ตั้ง"):
        title = "ภาควิชาวิศวกรรมไฟฟ้า"
        address = "คณะวิศวกรรมศาสตร์และเทคโนโลยีอุตสาหกรรม มหาวิทยาลัยศิลปากร"
        lati = 13.820267
        longi = 100.038116
        line_bot_api.reply_message(event.reply_token,
                                   LocationSendMessage(
                                       title=title,
                                       address=address,
                                       latitude=lati,
                                       longitude=longi))

@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)
            
if __name__ == "__main__":          
    app.run()

