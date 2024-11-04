# Xây dựng lớp tam giác (Triangle) có các thành phần: 3 cạnh a, b, c của một tam giác 
# và các phương thức:
# Nhập độ dài 3 cạnh của tam giác
# Xác định tam giác thuộc loại tam giác gì
# Tính chu vi của tam giác
# Tính diện tích của tam giác
import math
class triangle:
    def __init__(self,*args):
        self.a1,self.a2,self.a3 = args
        self.Type = self.typeTr()
        self.chuvi = self.tinh_chu_vi()
        self.dientich = self.tinh_dien_tich()
    def typeTr(self):
        a, b, c = sorted([self.a1, self.a2, self.a3])
        if a + b <= c:
            return "Không phải tam giác"
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            if c**2 == a**2 + b**2:
                return "Tam giác vuông cân"
            return "Tam giác cân"
        elif c**2 == a**2 + b**2:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"
        
    def tinh_chu_vi(self):
        return self.a1 + self.a2 + self.a3

    def tinh_dien_tich(self):
        s = self.tinh_chu_vi() / 2  # Nửa chu vi
        return math.sqrt(s * (s - self.a1) * (s - self.a2) * (s - self.a3))

    
#nhap
a,b,c = [int (i) for i in input("Nhap 3 canh tam giac: ").strip(" ").split()]
a= triangle(1,2,3)
print(a.__dict__)