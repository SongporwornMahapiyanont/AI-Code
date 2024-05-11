import google.generativeai as genai
from PIL import Image
import matplotlib.pyplot as plt

genai.configure(api_key="xxx")
model = genai.GenerativeModel("gemini-pro-vision")

img = Image.open("image01.jpg")
prompt = "บรรยายภาพนี้"
print("prompt : ",prompt)

try:
    response = model.generate_content([img,prompt])
    print(response.text)
except:
    print("no response")
    
plt.imshow(img)
plt.show()

