# Bài 3. Viết chương trình Python để tạo một lớp đại diện cho giỏ hàng 
# (ShoppingCart). Bao 
# gồm các phương pháp thêm (add_item) và xóa (remove_item) các mặt hàng cũng như tính 
# tổng giá (calculate_total). 
from os import *
class item:
    def __init__(self,name,price):
        self.MatHang = name
        self.Gia = price
class ShoppingCart:
    def __init__(self):
        self.Now = []
    
    def Add_ShoppingCart(self, *args):
        self.Now.extend(args)
    def Remove_item(self,a):
        if a in self.Now:
            self.Now.remove(a)
            print ("San pham da bi xoa khoi gio hang")
        else: print("Khong tim thay san pham!")
    
    def ShowCart(self):
        for i in self.Now:
            print (f"Ten: {i.MatHang}    Gia: {i.Gia}")
    def Calculate_total(self):
        sum = 0
        for i in self.Now:
            sum+=i.Gia
        return sum

if __name__ == "__main__":
    cart = ShoppingCart()
    while 1:
        print ("1. Them")
        print ("2. Thoat")
        z= int(input("\t OPTION: ").strip(" "))
        if z == 1:
            s = input("Nhap ten san pham va gia(cách nha dấu phẩy): ").strip(" ").split(",")
            a = item(s[0],int(s[1].strip(" ")))
            cart.Add_ShoppingCart(a)
            system("cls")
        else: 
            system(cls)
            break
    cart.ShowCart()
    print("Cost: {}".format(cart.Calculate_total()))
    
    
