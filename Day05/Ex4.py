# Đọc file văn bản chứa các số nguyên. Tính tổng, tích, hiệu, thương và ghi vào file csv
import os
import csv
path = os.getcwd() + r"\Day05\Data\dataex4.txt"
try:
    with open(path, "r") as file:
       s = file.read().split()
except FileNotFoundError:
    print ("Khong thay file!")

try:
    with open(os.getcwd()+ r"\Day05\output\Ex4_classwork.csv","w",encoding = "utf-8",newline="") as file:
        header = ["Cộng","Trừ","Nhân","Chia"]
        data = dict.fromkeys(header)
        data["Cộng"] = str(eval(f"{s[0]} + {s[1]}"))
        data["Trừ"] = str(eval(f"{s[0]} - {s[1]}"))
        data["Nhân"] = str(eval(f"{s[0]} * {s[1]}"))
        data["Chia"] = str(eval(f"{s[0]} / {s[1]}"))
        l = [data]
        writer = csv.DictWriter(file,fieldnames = header)
        writer.writeheader()
        writer.writerows(l)
except FileNotFoundError:
    print ("Khong thay file!")