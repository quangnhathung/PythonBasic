# Bài 1. Quản Lý Danh Sách Học Sinh:
#  Xây dựng một ứng dụng quản lý danh sách học sinh với các thao tác CRUD (Tạo, Đọc, 
# Cập nhật, Xóa).
#  Dữ liệu ban đầu sẽ được tạo ngẫu nhiên với các thông tin như tên, tuổi, giới tính, 
# lớp học, điểm số, v.v.
#  Người dùng có thể thêm mới, xem danh sách, cập nhật thông tin và xóa học sinh khỏi 
# danh sách
#  Dữ liệu sẽ được lưu trữ trong một tệp JSON.
from random import choice
from os import getcwd
import json
names = [
    "Nguyễn Văn An", "Trần Thị Bích","Lê Minh Phương","Phạm Quốc Khánh", "Hoàng Thị Hương",
    "Vũ Đức Tài","Đặng Thị Lan", "Ngô Thanh Sơn","Bùi Văn Nam","Phan Ngọc Dũng","Đỗ Thị Hoa",
    "Dương Văn Tú","Lý Thị Thanh","Lưu Ngọc Phú","Phùng Đức Hòa", "Hà Thị Ngọc", "Phạm Bích Nguyệt",
    "Nguyễn Tiến Mạnh","Vương Quốc Bảo", "Mai Hoàng Nam"
]
ages = [
    19, 20, 18, 21, 22,
    19, 20, 18, 20, 21,
    19, 20, 18, 19, 22,
    21, 20, 19, 18, 22
]
classes = [
    "10DHTH01", "10DHTH02", "11DHTH03", "11DHTH04", "12DHTH05",
    "12DHTH06", "13DHTH07", "13DHTH08", "14DHTH09", "14DHTH10",
    "15DHTH11", "15DHTH12", "10DHTH13", "10DHTH14", "11DHTH15",
    "12DHTH01", "13DHTH02", "14DHTH03", "15DHTH04", "10DHTH05"
]
scores = [
    7.5, 8.0, 6.0, 9.5, 4.5,
    5.0, 6.5, 7.0, 8.5, 9.0,
    5.5, 4.0, 7.8, 6.2, 8.3,
    6.7, 7.3, 9.1, 5.6, 10.0
]

class SinhVien:
    def __init__(self, ten, tuoi,lop, diem):
        self.Ten = ten
        self.Tuoi = tuoi
        self.Lop = lop
        self.Diem = diem
    def __str__(self):
        return f"Tên: {self.Ten}, Tuổi: {self.Tuoi}, Lớp: {self.Lop}, Điểm: {self.Diem}"

class Student_Manager:
    def __init__(self):
        self.list = []
    
    def add(self,a):
        self.list.append(a)
        
    def read(self):
        if not self.list:
            print("Danh sách trống.")
        else:
            print("Danh sách sinh viên:")
            for student in self.list:
                print(student)

    def update(self, ten, new_ten=None, new_tuoi=None, new_lop=None, new_diem=None):
        found = False
        for student in self.list:
            if student.Ten == ten:
                if new_ten:
                    student.Ten = new_ten
                if new_tuoi:
                    student.Tuoi = new_tuoi
                if new_lop:
                    student.Lop = new_lop
                if new_diem:
                    student.Diem = new_diem
                found = True
                break
        if not found:
            print(f"Không tìm thấy sinh viên có tên: {ten}")
            
    def delete(self, ten):
        initial_len = len(self.list)
        self.list = [student for student in self.list if student.Ten != ten]
        if len(self.list) < initial_len:
            print(f"Đã xóa sinh viên có tên: {ten}")
        else:
            print(f"Không tìm thấy sinh viên có tên: {ten}")

if __name__ == "__main__":
    manager = Student_Manager()
    for _ in range(100):
        a= SinhVien(choice(names),choice(ages),choice(classes),choice(scores))
        manager.add(a)
    
    try:
        path = getcwd() + r"\Day06\output\Ex1_homework.json"
        key = ["Tên","Tuổi","Lớp","Điểm"]
        data =[]
        for i in manager.list:
            dic = dict.fromkeys(key,None)
            dic["Tên"] = i.Ten
            dic["Tuổi"] = i.Tuoi
            dic["Lớp"] = i.Lop
            dic["Điểm"] = i.Diem
            data.append(dic)
        with open (path, "w", encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii= False, indent=4)
        
    except FileNotFoundError:
        print("Khong tim thay file ")
