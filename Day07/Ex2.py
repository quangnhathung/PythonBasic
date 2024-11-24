# Bài 2: Tìm kiếm từ trong câu
# Viết một chương trình Python để kiểm tra xem một từ cụ thể có xuất hiện trong một câu hay 
# không
import re
text = "Viết một chương trình Python để kiểm tra xem một từ cụ thể có xuất hiện trong một câu hay # không"

pattern = input("Nhap tu tim kiem: ").strip()
if pattern in text:
    print ("ok")
else: print("khong")