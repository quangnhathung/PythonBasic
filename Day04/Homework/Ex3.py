# Bài 3. Xây dựng một chương trình quản lý thông tin sinh vien bao gồm mã sinh vien và họ
# và tên. Thực hiện các thao tác thêm, xóa, sửa, và xem danh sách sinh vien.

class Student:
    def __init__(self, MaSv, Ten):
        self.MaSv = MaSv
        self.Ten = Ten

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, MaSv, Ten):
        if any(student.MaSv == MaSv for student in self.students):
            print("Ma sinh vien đa ton tai.")
        else:
            new_student = Student(MaSv, Ten)
            self.students.append(new_student)
            print("Thanh cong.")

    def removeStd(self, MaSv):
        
        for student in self.students:
            if student.MaSv == MaSv:
                self.students.remove(student)
                print("Xoa sinh vien Thanh cong.")
                return
        print("Khong tim thay sinh vien với mã này.")

    def edit_student(self, MaSv, new_Ten):
        for student in self.students:
            if student.MaSv == MaSv:
                student.Ten = new_Ten
                print("Thanh cong.")
                return
        print("Khong ton tai!")

    def Showstudents(self):
        if not self.students:
            print("Empty!!")
        else:
            print("Danh sach sinh vien:")
            for student in self.students:
                print(f"Ma SV: {student.MaSv}, Ho va ten: {student.Ten}")

