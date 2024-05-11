import openai

openai.api_key = "xxx"

model_use = "text-davinci-003"
# https://platform.openai.com/docs/models/gpt-3-5

prompt_text = "เขียนโปรแกรมเชื่อมต่อกล้องเว็บแคมด้วย python และ opencv"
#prompt_text = "แปลไปเป็นภาษาอังกฤษ ฉันชอบกินน้ำเย็น"
#prompt_text = "เขียนอีเมล์นัดคณะกรรมการประชุม วันที่ 18 มีนาคม 2566 เวลา 15.00 น."

response = openai.Completion.create(
    model=model_use,
    prompt=prompt_text,  
    max_tokens=1024) # max 4096

response_text = response.choices[0].text 
print(response_text)
