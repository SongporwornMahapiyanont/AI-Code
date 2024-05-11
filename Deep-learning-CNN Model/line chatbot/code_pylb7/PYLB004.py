import random
        #  0     1      2      3     4     5
color = ["แดง","เขียว","น้ำเงิน","เหลือง","ดำ","ขาว"]
print("color =",color)
print(len(color)) # 6
                     
idx = random.randint(0,len(color)-1) # สุ่ม 0 ถึง 5(6-1)
print("idx =",idx)
print(color[idx])
