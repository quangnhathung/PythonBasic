# Bài 7: Thay thế từ cụ thể trong đoạn văn: Sử dụng hàm re.sub để thay thế tất cả các lần xuất 
# hiện của một từ cụ thể trong đoạn văn bằng một từ khác.

import re
import os

path = os.getcwd() + r"\Day05\Data\dataex2,3.txt"
with open(path, "r", encoding = "utf-8") as file:
    s = file.read()
print (s, end = "\n\n")
st = input("Nhap tu tim kiem: ").strip()
rst = input("Nhap tu thay the: ").strip()
print (re.sub(st,rst,s))