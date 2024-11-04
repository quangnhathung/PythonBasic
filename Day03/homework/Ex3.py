# Xây dựng lớp số phức có các thuộc tính: phần thực, phần ảo và các phương thức: 
#  Cộng, trừ, nhân, chia hai số phức
# #  Nhập 2 số phức và thực hiện các phép toán trên hai số phức, xuất ra kết quả.

class sophuc:
    def __init__(self, Thuc, Ao):
        self.Thuc = Thuc
        self.Ao = Ao

    def __add__(self, other):
        return sophuc(self.Thuc + other.Thuc, self.Ao + other.Ao)

    def __sub__(self, other):
        return sophuc(self.Thuc - other.Thuc, self.Ao - other.Ao)

    def __mul__(self, other):
        Thuc_part = (self.Thuc * other.Thuc) - (self.Ao * other.Ao)
        Ao_part = (self.Thuc * other.Ao) + (self.Ao * other.Thuc)
        return sophuc(Thuc_part, Ao_part)

    def __truediv__(self, other):
        giatri = (other.Thuc ** 2 + other.Ao ** 2)
        if giatri == 0:
            raise ValueError("Không thể chia cho số phức bằng 0.")
        Thuc_part = (self.Thuc * other.Thuc + self.Ao * other.Ao) / giatri
        Ao_part = (self.Ao * other.Thuc - self.Thuc * other.Ao) / giatri
        return sophuc(Thuc_part, Ao_part)

    def __str__(self):
        return f"{self.Thuc} + {self.Ao}i" if self.Ao >= 0 else f"{self.Thuc} - {abs(self.Ao)}i"

def input_complex():
    Thuc = float(input("Nhập phần thực: "))
    Ao = float(input("Nhập phần ảo: "))
    return sophuc(Thuc, Ao)

print("Nhập số phức thứ nhất:")
a = input_complex()
print("Nhập số phức thứ hai:")
b = input_complex()

# Thực hiện các phép toán
sum_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b

# Xuất kết quả
print(f"Kết quả cộng: {a} + {b} = {sum_result}")
print(f"Kết quả trừ: {a} - {b} = {sub_result}")
print(f"Kết quả nhân: {a} * {b} = {mul_result}")
print(f"Kết quả chia: {a} / {b} = {div_result}")
