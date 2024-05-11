import base64
import requests

def text2image(api_key,engine_id,prompt_text_en,filenameout):
    api_host  = "https://api.stability.ai"
    response = requests.post(f"{api_host}/v1/generation/{engine_id}/text-to-image",headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },json={
            "text_prompts": [
                {
                    "text": prompt_text_en
                }
            ],
            "cfg_scale": 7,
            "height": 512,
            "width": 512,
            "samples": 1,
            "steps": 30,
    })
    #==============================================================
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))
    #==============================================================
    data = response.json()
    #==============================================================
    for i, image in enumerate(data["artifacts"]):
        with open(f"./"+filenameout, "wb") as f:
            f.write(base64.b64decode(image["base64"]))

def image2image(api_key,engine_id,prompt_text_en,filenamein,filenameout):
    api_host  = "https://api.stability.ai"
    response = requests.post(f"{api_host}/v1/generation/{engine_id}/image-to-image",headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },files={
            "init_image": open("./"+filenamein, "rb")
        },data={
            "image_strength": 0.35,
            "init_image_mode": "IMAGE_STRENGTH",
            "text_prompts[0][text]": prompt_text_en,
            "cfg_scale": 7,
            "samples": 1,
            "steps": 30,
        })
    #==============================================================
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))
    #==============================================================
    data = response.json()
    #==============================================================
    for i, image in enumerate(data["artifacts"]):
        with open(f"./"+filenameout, "wb") as f:
            f.write(base64.b64decode(image["base64"]))



    
