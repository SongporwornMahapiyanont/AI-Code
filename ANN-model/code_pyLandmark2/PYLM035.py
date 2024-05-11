from csv import writer
text = ['ant','cat','dog']
print(text)
with open('test1.csv','w',encoding='UTF8',newline='') as f:
    writer_f = writer(f)
    writer_f.writerow(text)
    f.close()
