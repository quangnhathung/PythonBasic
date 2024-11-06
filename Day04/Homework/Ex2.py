#Viết chương trình giải phương trình bậc 2: aX2+bX+c=0
from math import *

def phuongtrinh(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        return f"Hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Nghiệm kép: x = {x}"
    else:
        return "Phương trình vô nghiệm"

if __name__ == '__main__':
    a,b,c = map(int,input("Nhap a,b,c: ").split()) 
    ket_qua = phuongtrinh(a, b, c)
    print(ket_qua)