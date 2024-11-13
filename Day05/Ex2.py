# Bài 2. Đọc dữ liệu từ file văn bản, đảo ngược các từ trong mỗi dòng và ghi kết quả vào 
# file văn bản.
# Yêu cầu:
# 1. Tạo một file văn bản chứa các câu, mỗi câu nằm trên một dòng và có thể chứa nhiều 
# từ, các từ cách nhau bởi dấu cách.
# 2. Viết một chương trình Python để đọc dữ liệu từ file, đảo ngược các từ trong mỗi câu 
# và ghi kết quả vào file khác.
# 3. Xử lý lỗi: Bắt các ngoại lệ có thể xảy ra khi đọc file và xử lý chuỗi.

import os

path = os.getcwd() + r"\Day05\Data\dataex2,3.txt"
try:
    with open(path, "r", encoding = "utf-8") as file:
       s = file.read()
except FileNotFoundError:
    print ("Khong thay file!")

try:
    with open(os.getcwd()+ r"\Day05\output\Ex2_classwork.txt","w",encoding = "utf-8") as file:
        a= s.splitlines()
        line = []
        for i in a:
            a1 = [x[::-1] for x in i.split()]
            l = " ".join(a1)
            line.append(l)
        string = "\n".join(line)
        file.write(string)
except FileNotFoundError:
    print ("Khong thay file!")



