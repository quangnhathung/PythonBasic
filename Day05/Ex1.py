# Bài 1. Đọc dữ liệu từ file văn bản, tính tổng các số nguyên và ghi kết quả vào file văn bản.
# Yêu cầu:
# 1. Tạo một file văn bản chứa các số nguyên trên mỗi dòng.
# 2. Viết một chương trình Python để đọc dữ liệu từ file, tính tổng các số nguyên và ghi 
# kết quả vào file khác.
# 3. Xử lý lỗi: Bắt các ngoại lệ có thể xảy ra khi đọc file và chuyển đổi chuỗi sang số
# nguyên.
import os

path = os.getcwd() + r"\Day05\Data\dataex1.txt"
try:
    with open(path, "r+") as file:
        s = file.read()
except FileNotFoundError:
    print ("Khong thay file!")

try:
    with open(os.getcwd()+ r"\Day05\output\Ex1_classwork.txt","w") as file:
        a = [int (i) for i in s.split()]
        file.write(str(sum(a)))
except FileNotFoundError:
    print ("Khong thay file!")