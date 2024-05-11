import requests
import json

url=requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
covid_obj=json.loads(url.content.decode("utf-8"))[0]
print(covid_obj)
print("--------------------------")

date = covid_obj['update_date']
new_case = covid_obj['new_case']
print("ข้อมูลโควิด ณ วันที่ " + date)
print("จำนวนผู้ติดเชื้อ " + str(new_case) + " คน")
