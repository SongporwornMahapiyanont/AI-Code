import GT
from PIL import Image
import matplotlib.pyplot as plt
from stability_ai import text2image

api_key   = "xxx"
engine_id = "stable-diffusion-v1-6"
filename_save = "image_out01.jpg"

prompt_text_th = "แมวกำลังเล่นลูกบอล"

try:
    prompt_text_en = GT.translate(prompt_text_th,'th','en') # th --> en
    print(prompt_text_th)
    print(prompt_text_en)
    text2image(api_key,engine_id,prompt_text_en,filename_save)
    img = Image.open(filename_save)
    plt.imshow(img)
    plt.show()
except:
    print("ลองใหม่อีกครั้ง")
