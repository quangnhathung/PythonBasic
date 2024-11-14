# Bài 8. Mô Phỏng Lựa Chọn Ngẫu Nhiên: Viết một chương trình mô phỏng việc lựa chọn 
# ngẫu nhiên từ một danh sách các mục. Chương trình sẽ cho phép người dùng chọn một mục 
# ngẫu nhiên từ danh sách đó
import random
choice = input("Nhap list: ").strip(" ").split()
choice = [int(i) for i in choice]
print(random.choice(choice))