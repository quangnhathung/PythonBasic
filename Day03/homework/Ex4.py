# Xây dựng một chương trình thêm, xóa và hiển thị các phần tử của danh sách bằng 
# cách sử dụng các lớp.
# Yêu cầu:
# 1. Tạo một lớp và sử dụng hàm tạo để khởi tạo các giá trị của lớp đó.
# 2. Tạo các phương thức thêm, xóa, hiển thị các phần tử trong danh sách và trả về các 
# giá trị tương ứng.
# 3. Tạo đối tượng cho lớp và sử dụng đối tượng để gọi hàm tương ứng tùy theo lựa chọn 
# của người dùng.
# 5. In danh sách kết quả cuối cùng.
# 6. Thoát chương trình
import os

a = []
while 1:
    os.system("cls")
    print ("0. Thoat")
    print ("1. Them phan tu")
    print ("2. Xoa Phan tu")
    print ("3. Hien thi danh sach.")
    z = int (input("OPTION: "))
    print(end = "\n")
    if (z==0): break
    elif z==1: 
        n = [i for i in input("Nhap phan tu them: ").strip(" ").split()]
        a.extend(n)
    elif z==2:
        for i in a:
            print (i,end=" ")
        print()
        x = int (input("Phan tu ban muon xoa o vi tri thu may nao: "))
        a.pop(x-1)
    elif z==3:
        for i in a:
            print (i,end=" ")
        print()
        os.system("pause")
        
    
