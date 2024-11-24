# Bài 3: Phân tách chuỗi văn thành các câu
# Viết một chương trình Python để phân tách một đoạn văn từ file văn bản text.txt thành các 
# câu.
import re
import os

path = os.getcwd() + r"\Day05\Data\dataex2,3.txt"
with open(path, "r", encoding = "utf-8") as file:
    s = file.read()
    l = s.split('\n')
print (l)