# Bài 6. Viết một lớp có tên là Pass_manager. Lớp này phải có một danh sách tên là 
# old_passwords chứa tất cả mật khẩu trước đây của người dùng. Mục cuối cùng của
# danh sách là mật khẩu hiện tại của người dùng. Cần có một phương thức gọi là 
# get_password để trả về mật khẩu hiện tại và một phương thức gọi là set_password
# để đặt mật khẩu của người dùng. Phương thức set_password chỉ nên thay đổi mật khẩu
# nếu mật khẩu đã thử khác với tất cả mật khẩu trước đây của người dùng.
# Cuối cùng, tạo một phương thức có tên is_Corr để nhận một. chuỗi và trả về giá trị
# boolean Đúng hoặc Sai tùy thuộc vào việc chuỗi đó có bằng mật khẩu hiện tại hay không.
from os import system
from time import sleep
class Pass_Manager:
    def __init__(self):
        self.old_passworlds= []
    def get_passworld(self):
        return self.old_passworlds[len(self.old_passworlds)-1]
    def set_passworld(self):
        while 1:
            password = input("Nhap mat khau: ")
            if password in self.old_passworlds: 
                print ("\tMat khau da ton tai!")
                sleep(2)
                system("cls")
            else: break
        self.old_passworlds.append(password)
        print ("Done!")
        sleep(2)
        system("cls")
    def Enter_passworld(self,password):
        if password != self.get_passworld(): return False
        return True

user = Pass_Manager()
user.set_passworld()
user.set_passworld()
user.set_passworld()
user.set_passworld()
print("Pass hien tai: ", user.get_passworld())
print(user.Enter_passworld("05112005"))