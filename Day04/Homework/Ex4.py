'''Bài 4. Xây dựng ứng dụng quản lý danh sách các giao dịch:
Mô tả:Hệ thống quản lý 2 loại giao dịch:
 Giao dịch vàng: Mã giao dịch, ngày giao dịch (ngày/tháng/năm), đơn giá, số lượng, 
loại vàng có 3 loại 18k, 24k, 9999. Thành tiền được tính như sau: thành tiền = số lượng 
* đơn giá.
 Giao dịch tiền tệ: Mã giao dịch, ngày giao dịch (ngày/tháng/năm), tỷ giá (cũng là đơn 
giá), số lượng, loại tiền tệ có 3 loại:USD, EUR, AUD, loại giao dịch mua/bán. Thành 
tiền được tính như sau:
 Nếu loại giao dịch là “mua”thì: thành tiền = số lượng * tỷ giá
 Nếu loại giao dịch là “bán” thì: thành tiền = (số lượng * tỷ giá)* 1.05

Dựa vào mô tả trên, hãy:
(1) Tạo lớp GiaoDich với các thuộc tính và phương thức chung (giao dịch vàng cũng là 
giao dịch).
(2) Tạo lớp GiaoDichTienTe kế thừa từ lớp GiaoDich với các thuộc tính riêng và phương 
thức cần thiết.
(3) Nhập xuất danh sách các giao dịch.
(4) Tính tổng số lượng cho từng loại.
(5) Tính tổng thành tiền cho từng loại.'''
import os
from datetime import datetime
class GiaoDich:
    def __init__(self,magd,ten,date,gia,soluong):
        self.Ma = magd
        self.Ngaygiaodich = date
        self.Loai = ten
        self.Dongia = gia
        self.SoLuong = soluong
    def Thanhtien(self):
        return self.Dongia*self.SoLuong
    def ShowInfo(self):
        print (f"{self.Ma} - {self.Ngaygiaodich} - {self.Loai} - {self.SoLuong} - {self.Dongia} - ",end = "")
    
class GiaoDichTienTe(GiaoDich):
    def __init__(self,magd,ten,date,gia,soluong):
        super().__init__(magd,ten,date,gia,soluong)
    def Ban(self):
        return self.Dongia*self.SoLuong*1.05

if __name__ == "__main__":
    count = 1
    print ("QUẢN LÝ GIAO DỊCH:")
    while 1:
        magd = "GD00" + str(count)
        count+=1
        ngay = str(datetime.now().date())
        soluong = int(input("Nhap so luong: "))
        typeGd = int(input("Chon loai giao dich_1. Vang___2. Tien te: ").strip())
        if typeGd == 1:
            loai = input("Chon loai (18k/24k/9999): ").strip()
            gia = int(input("Nhap don gia: "))
            Gd = GiaoDich(magd,loai,ngay,gia,soluong)
            Gd.ShowInfo()
            print("Thanh tien : ",Gd.Thanhtien())
        elif typeGd == 2:
            loai = input("Chon loai (USD / EUR/ AUD): ").strip()
            gia = int(input("Nhap ty gia: "))
            Gd = GiaoDichTienTe(magd,loai,ngay,gia,soluong)
            typemuaban = int(input("Ban mua hay ban?_1. Mua___2. Ban: ").strip())
            if typemuaban == 1:
                Gd.ShowInfo()
                print("Thanh tien : ",Gd.Thanhtien())
            if typemuaban == 2:
                Gd.ShowInfo()
                print("Thanh tien : ",Gd.Ban())
        cont = int(input("Ban co muon tiep tuc giao dich?_1. Tiep tuc___0. Khong: ").strip())
        if (cont == 0): break
        os.system("cls")