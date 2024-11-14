# Bài 9. Đổi Chỗ Ngẫu Nhiên trong Danh Sách: Viết một chương trình đổi chỗ ngẫu nhiên các 
# phần tử trong một danh sách và in ra danh sách sau khi đã đổi chỗ.

import random

i = random.randint(1,6)
j = random.randint(1,6)
n = int (input("Nhap n: ").strip())
l = [random.randint(0,100) for i in range(n)]
print(l)
l.sort()
print (l)
l[i],l[j]=l[j],l[i]
print (l)