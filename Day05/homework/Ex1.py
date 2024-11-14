# Câu 1. Xây dựng một lớp lớp người (Person). Bao gồm các thuộc tính như tên, quốc gia và 
# ngày sinh và các phương thức:
#  Xác định tuổi của người đó.
#  In ra thông tin của người đó:
#      Xây dựng file input.json bao gồm mảng thông tin của nhiều người. Mỗi người gồm 
# các thuộc tính: name, country, birthday.
#  Đọc file này thành một list của các đối tượng Person.
#  Xây dựng chức năng: Thêm một người vào danh sách, Xóa người dựa trên tên, Xuất 
# ra danh sách người có tuổi cho trước.
#  Xử lý lỗi khi cần thiết.
from datetime import *
import os
import json

class Person:
    def __init__(self,ten,ngaysinh,quocgia):
        self.Ten = ten
        self.QuocTich = quocgia
        self.Birthday = ngaysinh #dd-mm-yyyy
        
    def Get_age(self):
        now = int(datetime.now().date().year)
        birthyear = datetime.strptime(self.Birthday,"%Y-%m-%d")
        year = birthyear.year
        self.age =  now - year

try:
    path = os.getcwd() + r"\Day05\Data\homework\dataEx1.json"
    with open(path, "r", encoding = "utf-8") as file:
        data = json.load(file)
        personlist = []
        for i in data:
            a = Person(i["name"],i["date_of_birth"],i["country"])
            personlist.append(a)
        for i in personlist:
            i.Get_age()
except FileNotFoundError:
    print ("Khong tim thay file!")
    
try:
    path = os.getcwd() + r"\Day05\output\homework\Ex1.json"
    with open(path, "w", encoding = "utf-8") as file:
        dictdata =[]
        key = ["Tên","Ngày Sinh", "Quốc tịch","Tuỏi"]
        for i in personlist:
            dic = dict.fromkeys(key)
            dic["Tên"] = i.Ten
            dic["Ngày Sinh"] = i.Birthday
            dic["Quốc tịch"] = i.QuocTich
            dic["Tuỏi"] = i.age
            dictdata.append(dic)
        json.dump(dictdata, file,ensure_ascii=False, indent=4)
        
except FileNotFoundError:
    print ("Khong tim thay file!")