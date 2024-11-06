# Bài 8. Tạo một lớp có tên là Giỏ hàng và thực hiện các thao tác sau:
# (1) Tạo một hàm tạo không có đối số và đặt thuộc tính tổng bằng 0, đồng thời khởi tạo 
# một thuộc tính dict trống có tên là items.
# (2) Tạo một phương thức add_item yêu cầu các đối số item_name, số lượng và giá. 
# Phương pháp này sẽ cộng chi phí của các hạng mục được thêm vào và giá trị tổng hiện 
# tại. Nó cũng nên thêm một mục nhập vào lệnh của các mục sao cho khóa là item_name 
# và giá trị là số lượng của mục đó.
# BM KHDL&TTNT 
# (3) Tạo một phương thức Remove_item yêu cầu các đối số tương tự như add_item. Nó sẽ
# loại bỏ các mặt hàng đã được thêm vào giỏ hàng và không cần thiết. Phương pháp này 
# sẽ khấu trừ chi phí của các mặt hàng đã xóa khỏi tổng số hiện tại và cũng cập nhật chính 
# sách các mặt hàng tương ứng.
# (4) Nếu số lượng của một mặt hàng cần loại bỏ vượt quá số lượng hiện tại của mặt hàng 
# đó trong giỏ hàng, giả định rằng tất cả các mục của mặt hàng đó sẽ bị xóa.
# (5) Tạo phương thức thanh toán nhận tiền mặt_đã thanh toán và trả về giá trị số dư từ
# khoản thanh toán. Nếu tiền mặt_đã thanh toán không đủ để thanh toán tổng số tiền, hãy 
# trả về "Tiền mặt thanh toán không đủ".
# (6) Tạo một lớp có tên Shop có hàm tạo không có đối số và khởi tạo thuộc tính có tên số
# lượng ở mức 100. Đảm bảo Shop kế thừa từ ShopCart.
# (7) Trong lớp Shop, ghi đè phương thức Remove_item, chẳng hạn như gọi Remove_item 
# của Shop mà không có đối số sẽ giảm số lượng đi một.
from os import system
from time import sleep
class item:
    def __init__(self,ten,gia,soluong):
        self.Ten = ten
        self.SoLuong = soluong
        self.Gia = gia
    def Cost(self):
        return self.SoLuong*self.Gia
class ShopCart:
    def __init__(self):
        self.Tong = 0
        self.Items = []
    def index(self,itm):
        for i in range(len(self.Items)):
            if itm.Ten.casefold() == self.Items[i].Ten.casefold(): return i
        return -1
    def add_item(self,itm):
        if any(itm.Ten.casefold() == i.Ten.casefold() for i in self.Items):
            i = self.index(itm)
            if i == -1: return
            self.Items[i].SoLuong += itm.SoLuong
        else: self.Items.append(itm)
    def index1(self,name):
        for i in range(len(self.Items)):
            if name.casefold() == self.Items[i].Ten.casefold(): return i
        return -1
    def Remove_item(self, name, soluong = 1):
        if any(name.casefold() == i.Ten.casefold() for i in self.Items):
            i = self.index1(name)
            if i == -1: return
            if self.Items[i].SoLuong > soluong:
                self.Items[i].SoLuong -= soluong
            else: self.Items.remove(self.Items[i])
        else: print("San pham khong ton tai!")

    def Thanh_Toan(self,tien):
        for i in self.Items:
            print(f'{i.SoLuong}*{i.Gia}')
            self.Tong += i.SoLuong * i.Gia
        if tien < self.Tong : print("So du khong du!")
        else:
            print("Thối lại: ", tien-self.Tong )
    
class Shop(ShopCart):
    def __init__(self):
        super().__init__()
    def Remove_item(self, name, soluong = 1):
        if any(name.casefold() == i.Ten.casefold() for i in self.Items):
            i = self.index1(name)
            if i == -1: return
            if self.Items[i].SoLuong > soluong:
                self.Items[i].SoLuong -= soluong
            else: self.Items.remove(self.Items[i])
        else: print("San pham khong ton tai!")
    def showcart(self):
        print ("Shopping Cart: ")
        for i in self.Items:
            print(f'[{i.Ten}, {i.Gia}, {i.SoLuong}]',end = "; ") 

if __name__ == "__main__":
    cart = Shop()
    while 1:
       
        cart.showcart()
        print()
        print ("1. Them")
        print ("2. Xoa mat hang")
        print ("3. Thanh toan")
        print ("4. Thoat")
        z= int(input("\t OPTION: ").strip(" "))
        if z == 1:
            s = input("Nhap ten san pham, gia va so luong(cách nhau dấu phẩy): ").strip(" ").split(",")
            a = item(s[0],int(s[1].strip(" ")),int(s[2].strip(" ")))
            cart.add_item(a)
            system("cls")
        elif z==2:
            remove = input("Nhap ten va so luong mat hang muon xoa(cách nhau dấu phẩy): ").strip().split(",")
            if len(remove) == 1: cart.Remove_item(remove[0])
            else: cart.Remove_item(remove[0],int(remove[1]))
            print("Done!")
            sleep(1)
            system('cls')
        elif z==3:
            money = int(input("Tiền đã đưa: "))
            cart.Thanh_Toan(money)
            sleep(10)
            system('cls')
        elif z==0: 
            sleep(5)
            system('cls')
            break