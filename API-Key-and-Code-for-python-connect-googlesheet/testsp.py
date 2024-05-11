import gspread
import time
sa = gspread.service_account(filename="lnc-bot-d4139cd6a05a.json")
sh = sa.open("lncbot")
wks = sh.worksheet("sheet1")

dt = time.localtime()
datedate = str(dt[2]) + "/" + str(dt[1]) + "/" + str(dt[0])
timetime = str(dt[3]) + ":" + str(dt[4]) + ":" + str(dt[5])
print(datedate)
print(timetime)

wks.append_row([datedate,timetime])
