import GT
# เรียกใช้ไลบรารี googletrans สำหรับการแปลภาษา

text_en = 'There are four cats on the table.'
print(text_en)

text_th = GT.translate(text_en,'en','th') # en --> th
print(text_th)
