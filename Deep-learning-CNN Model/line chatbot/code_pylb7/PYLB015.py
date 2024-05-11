text = "คำนวณ 4+6"
print(text)

result = text.startswith("คำนวณ") # "คำนวณ 4+6" ใช่ True
print(result)

text_cut = text.strip("คำนวณ") # " 4+6"
print(text_cut)

text_cut = text_cut.replace(" ", "") # "4+6"
print(text_cut)
