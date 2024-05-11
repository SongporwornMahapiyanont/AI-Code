from flask import Flask, request, send_from_directory
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            FlexSendMessage,
                            BubbleContainer,
                            BoxComponent,
                            TextComponent,
                            ButtonComponent,
                            BubbleStyle,
                            BlockStyle,
                            MessageAction,
                            URIAction)

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
#---------------------------------------------------------------------------     
    if text == 'A': # มี 1 ปุ่ม primary
        flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[ButtonComponent(style='primary', # primary,secondary,link
                                          color='#016c9a',
                                          height='sm', # sm,*md
                                          action=MessageAction(
                                              label='เชิญกดปุ่มได้เลยครับ',
                                              text='คุณได้กดปุ่มแล้ว'))]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------     
    if text == 'B': # มี 1 ปุ่ม secondary
        flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[ButtonComponent(style='secondary', # primary,secondary,link
                                          color='#e36743',
                                          action=MessageAction(
                                              label='เชิญกดปุ่มได้เลยครับ',
                                              text='คุณได้กดปุ่มแล้ว'))]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------     
    if text == 'C': # มี 1 ปุ่ม link
        flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[ButtonComponent(style='link', # primary,secondary,link
                                          color='#e36743',
                                          action=MessageAction(
                                              label='เชิญกดปุ่มได้เลยครับ',
                                              text='คุณได้กดปุ่มแล้ว'))]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------     
    if text == 'D': # มี 2 ปุ่ม primary แนวตั้ง
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[ButtonComponent(style='primary', # primary,secondary,link
                                          color='#e36743',
                                          action=MessageAction(
                                              label='กาแฟร้อน',
                                              text='คุณสั่งกาแฟร้อน')),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#2acaea',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='กาแฟเย็น',
                                              text='คุณสั่งกาแฟเย็น'))]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------         
    if text == 'E': # มี 2 ปุ่ม primary แนวนอน
        flex = BubbleContainer(
            size = 'mega', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='horizontal',
                contents=[ButtonComponent(style='primary', # primary,secondary,link
                                          color='#e36743',
                                          action=MessageAction(
                                              label='กาแฟร้อน',
                                              text='คุณสั่งกาแฟร้อน')),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#2acaea',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='กาแฟเย็น',
                                              text='คุณสั่งกาแฟเย็น'))]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------      
    if text == 'F': # มี 1 ข้อความ และ มี 2 ปุ่ม primary แนวตั้ง
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='เลือกเมนู',
                                        align='center', # *start,end,center
                                        color='#0000ff',
                                        weight='regular', # *regular,bold
                                        style='italic', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        ),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#cc4668',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='ไข่เจียว',
                                              text='คุณสั่งไข่เจียว')),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#61bdac',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='ผัดกระเพรา',
                                              text='คุณสั่งผัดกระเพรา'))]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------      
    if text == 'G': # มี 1 ข้อความ และ มี 2 ปุ่ม primary แนวตั้ง URIAction
        flex = BubbleContainer(
            size = 'mega', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='เลือกเมนู',
                                        align='center', # *start,end,center
                                        color='#0000ff',
                                        weight='regular', # *regular,bold
                                        style='italic', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        ),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#2acaea',
                                          margin = 'md',
                                          action=URIAction(
                                              label='ไปที่ Google',
                                              uri='https://www.google.com')),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#ff494d',
                                          margin = 'md',
                                          action=URIAction(
                                              label='ไปที่ youtube',
                                              uri='https://www.youtube.com')),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#ffc181',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='กดแล้วได้ข้อความ',
                                              text='สวัสดีวันจันทร์'))]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------  
if __name__ == "__main__":          
    app.run()

