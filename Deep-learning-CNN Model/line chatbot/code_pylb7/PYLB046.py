import os
from gtts import gTTS

text = 'พรุ่งนี้ไปเที่ยวที่ไหนกันดี'
print(text)

speak = gTTS(text=text, lang='th')

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp').replace("\\","/")
print(static_tmp_path)
filename_image = 'speak.mp3'
speak.save(static_tmp_path+'/'+filename_image) #บันทึกไฟล์เสียงลงห้อง tmp

print('แปลงข้อความเป็นเสียงพูดเรียบร้อยแล้ว')


