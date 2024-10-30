# Bài 1. Xây dựng một chương trình để tính diện tích và chu vi hình tròn.
# Yêu cầu:
# 1. Lấy giá trị bán kính hình tròn từ người dùng.
# 2. Tạo một lớp và sử dụng hàm tạo để khởi tạo các giá trị của lớp đó.
# 3. Tạo một phương thức gọi là diện tích/chu vi và trả về diện tích/chu vi của lớp.
# 4. In kết quả
# 5. Thoát
from math import *

class Circle:
    def __init__ (self, bankinh):
        self.Bankinh = bankinh
    def Dien_Tich(self):
        return (self.Bankinh ** 2) * pi
    def Chu_vi(self):
        return self.Bankinh * 2* pi
r = int(input("Nhap ban kinh: "))
Hinhtron= Circle(r)
print ("Dien tich la:", Hinhtron.Dien_Tich())
print ("Chu vi la:", Hinhtron.Chu_vi())