# Viết hàm tạo mảng số nguyên a với n phần tử và mảng b chỉ chứa các phần tử chẵn của a. 

a = list(input("Nhap mang a: ").split(" "))
a = [int (i) for i in a]
print (a)
b = [i for i in a if i % 2 == 0]
print (b)