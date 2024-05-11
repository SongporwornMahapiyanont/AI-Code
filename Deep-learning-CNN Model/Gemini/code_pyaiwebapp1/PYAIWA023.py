import google.generativeai as genai

genai.configure(api_key="xxx")

model = genai.GenerativeModel("gemini-pro")

while True:
    prompt = input("ป้อน prompt : ")
    try:
        response = model.generate_content(prompt)
        print(response.text)
    except:
        print("no response")
    


