# Câu 1. Xây dựng một lớp lớp người (Person). Bao gồm các thuộc tính như tên, quốc gia và 
# ngày sinh và các phương thức:
#  Xác định tuổi của người đó.
#  In ra thông tin của người đó:
from datetime import datetime

from datetime import datetime

class Person:
    def __init__(self):
        self.name = ''
        self.country = ''
        self.birth_date = ''

    def input_info(self):
        self.name = input("Nhập tên: ")
        self.country = input("Nhập quốc gia: ")
        birth_date_str = input("Nhập ngày sinh (dd-mm-yy)): ")
        self.birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y").date()  # Chuyển đổi chuỗi thành đối tượng date
        self.tuoi = self.age()
    def age(self):
        today = datetime.today().date()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age


a = Person()
a.input_info()   
print(a.__dict__)  


