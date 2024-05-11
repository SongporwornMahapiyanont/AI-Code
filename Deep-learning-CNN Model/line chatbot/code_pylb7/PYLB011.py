import GT
# เรียกใช้ไลบรารี googletrans สำหรับการแปลภาษา

text_th = 'สวัสดีครับ ผมเป็นนักเรียน'
print(text_th)

text_en = GT.translate(text_th,'th','en') # th --> en
print(text_en)
