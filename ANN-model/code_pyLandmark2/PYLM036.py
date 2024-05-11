from csv import writer
text = ['1','3','8']
print(text)
with open('test1.csv','a',encoding='UTF8',newline='') as f:
    writer_f = writer(f)
    writer_f.writerow(text)
    f.close()
