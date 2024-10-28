# Tạo một danh sách mới từ 2 danh sách sử dụng điều kiện sau.
# Cho 2 danh sách, viết hàm tạo một 
# danh sách mới sao cho danh sách mới chứa các số lẻ 
# từ danh sách đầu tiên và các số chẵn từ danh 
# sách thứ hai.

a = list(input("Nhập mảng 1:").split(" "))
a = [int (i) for i in a]
b = list(input("Nhập mảng 2:").split(" "))
b = [int (i) for i in b]
c= []
maxlenght = a if len(a)>len(b) else b
for i in range(len(maxlenght)):
    if (i<len(a if len(a)<len(b) else b)) :
        if a[i] %2 !=0: c.append(a[i])
        if b[i] %2 ==0: c.append(b[i])
    else:
        if len(a)>len(b):
            if a[i] % 2 != 0:
                c.append(a[i])
        else: 
            if b[i] % 2 == 0:
                c.append(b[i])
    
print ("Mang sau khi tron: ",c);