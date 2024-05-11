from flask import Flask, request, send_from_directory
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            FlexSendMessage,
                            BubbleContainer,
                            BoxComponent,
                            TextComponent,
                            BubbleStyle,
                            BlockStyle)

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
    if text == 'A': # มีข้อความเดียว
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#fffacb')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='สวัสดีครับ',
                                        align='center', # *start,end,center
                                        color='#0000ff',
                                        weight='regular', # *regular,bold
                                        style='italic', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        )]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------     
    if text == 'B': # มี 2 ข้อความ
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#fff2f4')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='สวัสดีครับ',
                                        align='start', # *start,end,center
                                        color='#0000ff',
                                        weight='regular', # *regular,bold
                                        style='italic', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        ),
                          TextComponent(text='ยินดีต้อนรับ',
                                        align='end',
                                        color='#ff4455',
                                        weight='regular',
                                        style='normal', 
                                        decoration='underline', 
                                        size='md' 
                                        )]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------
    if text == 'C': # มี 3 ข้อความ
        flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#ffffff')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='สวัสดีครับ',
                                        align='start', # *start,end,center
                                        color='#0000ff',
                                        weight='regular', # *regular,bold
                                        style='italic', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        ),
                          TextComponent(text='ยินดีต้อนรับ',
                                        align='center', 
                                        color='#c73a40',
                                        weight='regular', 
                                        style='italic', 
                                        decoration='underline', 
                                        size='xxl' 
                                        ),
                          TextComponent(text='หิวข้าวไหมครับ',
                                        align='end',
                                        color='#402717',
                                        weight='bold',
                                        style='italic', 
                                        decoration='line-through', 
                                        size='md' 
                                        )]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------
    if text == 'D': # แสดงค่าอุณหูมิ
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#d8facc')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='อุณหภูมิ',
                                        align='center', # *start,end,center
                                        color='#000000',
                                        weight='bold', # *regular,bold
                                        style='normal', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        ),
                          TextComponent(text='25',
                                        align='center',
                                        color='#416fec',
                                        weight='bold',
                                        style='normal', 
                                        decoration='none', 
                                        size='5xl' 
                                        )]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------
    if text == 'E': # แสดงค่าอุณหูมิ และ ความชื้น
        flex = BubbleContainer(
            size = 'mega', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#d8facc')),
            body = BoxComponent(
                layout='horizontal',
                contents=[BoxComponent(layout='vertical',
                                       contents=[
                                           TextComponent(text='อุณหภูมิ',
                                                         align='center',
                                                         color='#000000',
                                                         weight='bold',
                                                         style='normal',
                                                         decoration='none',
                                                         size='xl'
                                                         ),
                                           TextComponent(text='25',
                                                         align='center',
                                                         color='#416fec',
                                                         weight='bold',
                                                         style='normal', 
                                                         decoration='none', 
                                                         size='5xl' 
                                                          )]),
                          BoxComponent(layout='vertical',
                                       contents=[
                                           TextComponent(text='ความชื้น',
                                                         align='center',
                                                         color='#000000',
                                                         weight='bold',
                                                         style='normal',
                                                         decoration='none',
                                                         size='xl'
                                                         ),
                                           TextComponent(text='74',
                                                         align='center',
                                                         color='#38761d',
                                                         weight='bold',
                                                         style='normal', 
                                                         decoration='none', 
                                                         size='5xl' 
                                                          )])]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------
if __name__ == "__main__":          
    app.run()

