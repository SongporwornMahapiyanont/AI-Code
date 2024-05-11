from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            TemplateSendMessage,
                            MessageAction,
                            CarouselTemplate,
                            CarouselColumn)

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
       
    if text == 'วิชาเลือก':
        # กำหนดได้ไม่เกิน 10 อัน
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='618466',text='การประมวลผลภาพดิจิทัลเบื้องต้น', actions=[
                MessageAction(label='คำอธิบายรายวิชา',text='คำอธิบายรายวิชา 618466'),
                MessageAction(label='อาจารย์ผู้สอน', text='อาจารย์ผู้สอน 618466')]),
            
            CarouselColumn(title='618486',text='เส้นใยนำแสง', actions=[
                MessageAction(label='คำอธิบายรายวิชา',text='คำอธิบายรายวิชา 618486'),
                MessageAction(label='อาจารย์ผู้สอน', text='อาจารย์ผู้สอน 618486')]),
            
            CarouselColumn(title='618443',text='การสื่อสารข้อมูลและเครือข่ายคอมพิวเตอร์', actions=[
                MessageAction(label='คำอธิบายรายวิชา',text='คำอธิบายรายวิชา 618443'),
                MessageAction(label='อาจารย์ผู้สอน', text='อาจารย์ผู้สอน 618443')]),
        ])
        template_message = TemplateSendMessage(alt_text='Hello',
                                               template=carousel_template)
        line_bot_api.reply_message(event.reply_token,template_message)
        
    if text == 'คำอธิบายรายวิชา 618466':
        text_out = "พื้นฐานภาพดิจิทัล การปรับปรุงภาพ การกรองภาพ การหาขอบภาพ การแปลงทาง เรขาคณิตของภาพ แบบจำลองสี ลักษณะภาพ การแบ่งส่วนภาพ การแทนและอธิบายภาพ"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

    if text == 'อาจารย์ผู้สอน 618466':
        text_out = "อาจารย์ ดร.โสภณ ผู้มีจรรยา"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

    if text == 'คำอธิบายรายวิชา 618486':
        text_out = "พื้นฐานทางแสงและเส้นใยนำแสง พารามิเตอร์ของเส้นใยนำแสง คุณสมบัติของ เส้นใยนำแสง การเชื่อมต่อสายและการเชื่อมร่วมสาย แหล่งกำเนิดแสง ตัวตรวจจับแสง สัญญาณ รบกวนและการตรวจจับ การมอดูเลต การมัลติเพล็กซ์ทางความยาวคลื่น (ดับเบิลยูดีเอ็ม) การออกแบบระบบเส้นใยนำแสง"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

    if text == 'อาจารย์ผู้สอน 618486':
        text_out = "ผู้ช่วยศาสตราจารย์ ดร.ระพีพันธ์ แก้วอ่อน"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))
        
    if text == 'คำอธิบายรายวิชา 618443':
        text_out = "การสื่อสารข้อมูลและเครือข่ายคอมพิวเตอร์เบื้องต้น สถาปัตยกรรมเครือข่ายแบบลำดับชั้น โปรโตคอลและการเชื่อมต่อจุดต่อจุด สื่อที่ใช้ในการส่งข้อมูล การสื่อสารแบบเข้าถึงช่องสัญญาณได้หลายผู้ใช้ การตรวจสอบและแก้ไขความผิดพลาด การควบคุมและโปรโตคอลของการเชื่อมต่อข้อมูล ข่ายงานบริเวณเฉพาะที่ (แลน) ข่ายงานบริเวณกว้าง (แวน)"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

    if text == 'อาจารย์ผู้สอน 618443':
        text_out = "อาจารย์พรชัย เปลี่ยมทรัพย์"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))
         
if __name__ == "__main__":          
    app.run()

