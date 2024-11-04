# Bài 4. Viết một chương trình tạo lớp nhân viên gồm các thuộc tính: tên, tuổi, địa chỉ, tiền 
# lương, tổng số giờ làm và các phương thức 
#  inputInfo(): Nhập thông tin nhân viên từ bàn phím
#  printInfo(): In ra tất cả các thông tin nhân viên
#  tinhThuong(): Tính và trả về tiền thưởng của nhân viên theo công thức sau:
#  Nếu tổng số giờ làm của nhân viên >=200 thì thưởng=lương*20%
#  Nếu tổng số giờ làm của nhân viên <200 và >=100 thì thưởng=lương*10%
#  Nếu tổng số giờ làm của nhân viên <100 thì thưởng=0

class Nhanvien:
    def __init__(self):
        self.ten = ""
        self.tuoi = 0
        self.diachi = ""
        self.luong = 0
        self.tonggiolam = 0
        
    def inputInfo(self):
        self.ten = input("Ten nhan vien: ")
        self.tuoi = int(input("Tuoi: "))
        self.diachi = input("Dia chi: ")
        self.luong = float(input("Luong: "))
        self.tonggiolam = int(input("So gio lam viec: "))
    def thuong(self):
        if self.tonggiolam >= 200:
            self.thuong = self.luong * 0.2
        elif 100 <= self.tonggiolam < 200:
            self.thuong = self.luong * 0.1
        else:
            self.thuong = 0
a= Nhanvien()
a.inputInfo()
a.thuong()
print(a.__dict__)
