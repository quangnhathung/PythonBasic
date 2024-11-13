# Bài 3. Đọc dữ liệu từ file văn bản, tính tổng số từ trong mỗi dòng và ghi kết quả vào file văn 
# bản.
# Yêu cầu:
# 1. Tạo một file văn bản chứa các câu, mỗi câu có thể chứa nhiều từ, các từ cách nhau 
# bởi dấu cách.
# 2. Viết một chương trình Python để đọc dữ liệu từ file, tính tổng số từ trong mỗi câu và 
# ghi kết quả vào file khác.
# 3. Xử lý lỗi: Bắt các ngoại lệ có thể xảy ra khi đọc file và xử lý chuỗi.
import os

path = os.getcwd() + r"\Day05\Data\dataex2,3.txt"
try:
    with open(path, "r", encoding = "utf-8") as file:
       s = file.read()
except FileNotFoundError:
    print ("Khong thay file!")

try:
    with open(os.getcwd()+ r"\Day05\output\Ex3_classwork.txt","w",encoding = "utf-8") as file:
        file.write(str(len(s.split())))
except FileNotFoundError:
    print ("Khong thay file!")