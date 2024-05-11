import openai
import requests
from io import BytesIO
from PIL import Image
import os
import GT

openai.api_key = "xxx"

prompt_text_th = "แมว 4 ตัวกำลังนั่งอยู่บนโต๊ะ"
prompt_text_en = GT.translate(prompt_text_th,'th','en') # th --> en
print(prompt_text_th)
print(prompt_text_en)

response = openai.Image.create(
    prompt = prompt_text_en,
    n = 1, # ต้องการภาพ output กี่แบบ
    size = "512x512") # 256x256, 512x512, 1024x1024

img_url = response['data'][0]['url']
img_data = requests.get(img_url).content
img = Image.open(BytesIO(img_data))
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp').replace("\\","/")
print(static_tmp_path)
img.save(static_tmp_path+'/ai_image.jpg')
img.show()
