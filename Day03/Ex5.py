# Bài 5. Viết một chương trình tạo lớp sinh viên và lưu trữ cac thông tin cho một sinh viên: Mã 
# số sinh viên (10 ký tự), điểm trung bình từ 0 đến 10, tuổi phải lớn hơn hoặc bằng 18, Lớp 
# phải bắt đầu bằng Khóa học (12) - kế đến là 2 ký tự DH - kế đến chuyên ngành học (TH/MMT) 
# – cuối cùng là tên lớp có 2 chữ số từ 01 đến 99 (Ví dụ: 12DHTH02/12DHMMT04) và xây 
# dựng các phương thức:
#  Phương thức tạo
#  Phương thức inputInfo(): nhập thông tin sinh viên từ bàn phím
#  Phương thức showInfor(): hiển thị tất cả các thông tin của sinh viên
#  Phương thức xét xem sinh viên có được học bổng không? Biết rằng, nếu điểm trung 
# bình >=8 là được học bổng.

class SinhVien:
    def __init__(self):
        self.ma_so = ""
        self.diem_tb = 0.0
        self.tuoi = 0
        self.lop = ""
        self.hoc_bong = False

    def inputInfo(self):
        self.ma_so = input("Nhập mã số sinh viên (10 ký tự): ")
        while len(self.ma_so) != 10:
            print("Mã số sinh viên phải có đúng 10 ký tự.")
            self.ma_so = input("Nhập lại mã số sinh viên (10 ký tự): ")

        self.diem_tb = float(input("Nhập điểm trung bình (0-10): "))
        while not (0 <= self.diem_tb <= 10):
            print("Điểm trung bình phải từ 0 đến 10.")
            self.diem_tb = float(input("Nhập lại điểm trung bình (0-10): "))
        self.tuoi = int(input("Nhập tuổi sinh viên (>=18): "))
        while self.tuoi < 18:
            print("Tuổi sinh viên phải lớn hơn hoặc bằng 18.")
            self.tuoi = int(input("Nhập lại tuổi sinh viên (>=18): "))
        self.lop = input("Nhập lớp: ")
        while not self.kiem_tra_lop(self.lop):
            print("Không đúng định dạng.")
            self.lop = input("Nhập lại lớp: ")

        self.hoc_bong = self.xet_hoc_bong()

    def kiem_tra_lop(self, lop):
        if len(lop) == 8 and lop[:2] == "12" and lop[2:4] == "DH" and lop[4:6] in ["TH", "MMT"] and lop[6:].isdigit():
            return 1 <= int(lop[6:]) <= 99
        return False

    def xet_hoc_bong(self):
        return self.diem_tb >= 8

    def showInfo(self):
        print(f"Mã số sinh viên: {self.ma_so}")
        print(f"Điểm trung bình: {self.diem_tb}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Lớp: {self.lop}")
        print(f"Được học bổng: {'Có' if self.hoc_bong else 'Không'}")

# Sử dụng lớp SinhVien
sinh_vien = SinhVien()
sinh_vien.inputInfo()
sinh_vien.showInfo()
