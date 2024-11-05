# Bài 2. Tính chu vi & diệntích các hình (abstract)
# Viết chương trình tính chu vi và điện tích của một số hình như sau:
#  Hình tròn
#  Hình chữ nhật
#  Hình tam giác

import math

class HinhTron:
    def __init__(self, BanKinh):
        self.BanKinh = BanKinh

    def DienTich(self):
        return math.pi * (self.BanKinh ** 2)

    def ChuVi(self):
        return 2 * math.pi * self.BanKinh

class HinhTamGiac:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def DienTich(self):
        p = (self.a1 + self.a2 + self.a3) / 2
        return math.sqrt(p * (p - self.a1) * (p - self.a2) * (p - self.a3))

    def ChuVi(self):
        return self.a1 + self.a2 + self.a3

class HinhChuNhat:
    def __init__(self, Dai, Rong):
        self.Dai = Dai
        self.Rong = Rong

    def DienTich(self):
        return self.Dai * self.Rong

    def ChuVi(self):
        return 2 * (self.Dai + self.Rong)

#da hinh
def ChuVi(a):
    return a.ChuVi()
def DienTich(a):
    return a.DienTich()

a = HinhChuNhat(4,5)
print(ChuVi(a))
print (DienTich(a))