# Xây dựng một lớp phân số (Fraction) có các thuộc tính: Tử số, mẫu số và các phương 
# thức:
#  Phương thức tạo để khởi tạo giá trị cho tử số và mẫu số
#  Các phương nhập, xuất, rút gọn, nghịch đảo phân số
#  Các phương thức cộng (add), trừ (sub), nhân (mul), chia (div), hai phân số.

class Fraction:
    def __init__(self,a,b):
        self.tu =a
        self.mau =b
        self.print = str(a)+"/" + str(b)
    def ucln(self,a,b):
        while b:
            a, b = b, a % b
        return a
    def formatfraction(self):
        if self.mau < 0 and self.tu > 0:
            self.mau *=-1
            self.tu *= -1
        elif self.mau < 0 and self.tu < 0:
            self.mau *=-1
            self.tu *= -1
        
        ucln = self.ucln(self.tu,self.mau)
        self.tu/=ucln
        self.mau/=ucln
        self.print = str(int(self.tu))+"/" + str(int(self.mau))
        
    def add(self, other):

        new_tu = (self.tu * other.mau) + (other.tu * self.mau)
        new_mau = self.mau * other.mau
        return Fraction(new_tu, new_mau)

    def sub(self, other):
        new_tu = (self.tu * other.mau) - (other.tu * self.mau)
        new_mau = self.mau * other.mau
        return Fraction(new_tu, new_mau)

    def mul(self, other):
        new_tu = self.tu * other.tu
        new_mau = self.mau * other.mau
        return Fraction(new_tu, new_mau)

    def div(self, other):
        if other.tu == 0:
            raise ValueError("Không thể chia cho phân số bằng 0.")
        new_tu = self.tu * other.mau
        new_mau = self.mau * other.tu
        return Fraction(new_tu, new_mau)

    def __str__(self):
        return self.print

x,y = [int (i) for i in input("Nhap phan so (a/b): ").strip(" ").split("/")]
a= Fraction(x,y)
a.formatfraction()
print (a.print)