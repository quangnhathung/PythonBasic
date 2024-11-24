# Bài 4: Thay thế các từ trong đoạn văn và lưu kết quả vào file mới
# Viết một chương trình Python để thay thế một từ hoặc cụm từ cụ thể trong một đoạn văn đọc 
# từ file văn bản text.txt, sau đó lưu kết quả vào một file mới có tên là text_replaced.txt.

import re
import os

path = os.getcwd() + r"\Day05\Data\dataex2,3.txt"
with open(path, "r", encoding = "utf-8") as file:
    s = file.read()
print (s, end = "\n\n")
st = input("Nhap tu tim kiem: ").strip()
rst = input("Nhap tu thay the: ").strip()
print (re.sub(st,rst,s))