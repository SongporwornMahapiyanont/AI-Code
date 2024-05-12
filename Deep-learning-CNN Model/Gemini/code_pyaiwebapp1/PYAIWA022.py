import google.generativeai as genai

genai.configure(api_key="AIzaSyA0TwQnk0mKo9rgnty9z9l05hoz7F2dfmU")

model = genai.GenerativeModel("gemini-pro")

prompt = "แต่งนิทานที่มี ไก่ และ เป็ด"
print("prompt : ",prompt)

try:
    response = model.generate_content(prompt)
    print(response.text)
except:
    print("no response")
    


