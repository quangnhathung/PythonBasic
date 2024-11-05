# Bài 1. Tạo ba lớp, Person có 2 thuộc tính: name, age, Employee (Nhân viên) 
# có 2 thuộc tính: 
# emp_id, salary và Student (Sinh viên) có 2 thuộc tính: student_id , grade .
# Sử dụng nhiều kế thừa để tạo một lớp “PersonInfo” kế thừa từ cả “Nhân viên” 
# và “Sinh viên”. Thêm các thuộc tính và phương thức cụ thể cho từng lớp.

class Person:
    def __init__(self, name,age):
        self.Name = name
        self.Age = age

class Employee:
    def __init__(self,id1,salary):
        self.emp_id = id1
        self.salary = salary

class Student: 
    def __init__(self, ids, grade):
        self.student_id = ids
        self.grade =grade

class PersonInfo(Person, Employee, Student):
    def __init__(self,name,age,id1,salary,ids, grade):
        Person.__init__(self, name, age)
        Employee.__init__(self, id1,salary)
        Student.__init__(self, ids, grade)

a =  PersonInfo("John", 30, "E123", 50000, "S456", "A")

print (a.__dict__)
