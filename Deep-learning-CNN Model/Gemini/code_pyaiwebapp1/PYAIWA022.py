import google.generativeai as genai

genai.configure(api_key="xxx")

model = genai.GenerativeModel("gemini-pro")

prompt = "แต่งนิทานที่มี ไก่ และ เป็ด"
print("prompt : ",prompt)

try:
    response = model.generate_content(prompt)
    print(response.text)
except:
    print("no response")
    


