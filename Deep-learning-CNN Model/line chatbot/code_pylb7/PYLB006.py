from wit import Wit
wit_access_token = "xxx"
client = Wit(wit_access_token)

text = "สวัสดีครับผม"
#text = "อากาศข้างนอกเป็นอย่างไร"
#text = "วันนี้วันอะไรกันนะ"
#text = "ขอมุกตลก"
#text = "ขอเปิดไฟหน่อย"

print("text = ",text)

if (text != ""):
    ret = client.message(text)
    if len(ret["intents"]) > 0:
        confidence = ret["intents"][0]['confidence']
        
        if (confidence > 0.8):
            intents_name = ret["intents"][0]['name']        
            print("intent = ",intents_name)
        else:
            print("intent = unknow")
    else:
        print("intent = unknow")
