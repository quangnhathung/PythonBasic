#Thực hiện lại bài 4 nhưng kết quả ghi ra là file json.
import os
import json
path = os.getcwd() + r"\Day05\Data\dataex4.txt"
try:
    with open(path, "r") as file:
       s = file.read().split()
except FileNotFoundError:
    print ("Khong thay file!")

try:
    with open(os.getcwd()+ r"\Day05\output\Ex5_classwork.json","w",encoding = "utf-8",newline="") as file:
        header = ["Cộng","Trừ","Nhân","Chia"]
        data = dict.fromkeys(header)
        data["Cộng"] = str(eval(f"{s[0]} + {s[1]}"))
        data["Trừ"] = str(eval(f"{s[0]} - {s[1]}"))
        data["Nhân"] = str(eval(f"{s[0]} * {s[1]}"))
        data["Chia"] = str(eval(f"{s[0]} / {s[1]}"))
        json.dump(data,file,ensure_ascii=False,indent=4)
except FileNotFoundError:
    print ("Khong thay file!")
