# Viết một lớp có tên là Sản phẩm. Lớp này phải có các thuộc tính: số lượng và giá, tên 
# sản phẩm, số lượng mặt hàng của sản phẩm đó trong kho và giá thông thường của sản phẩm. 
# Cần có một phương thức get_price để nhận số lượng mặt hàng cần mua và trả về chi phí mua 
# nhiều mặt hàng đó, trong đó giá thông thường được tính cho các đơn hàng dưới 10 mặt hàng, 
# áp dụng giảm giá 10% cho các đơn hàng từ giữa 10 và 99 mặt hàng, giảm giá 20% cho đơn hàng 
# từ 100 mặt hàng trở lên. Cũng nên có một phương thức gọi là make_purchase để nhận số lượng 
# mặt hàng cần mua và giảm số lượng đó đi.

class SanPham:
    def __init__(self, ten_san_pham, so_luong, gia_thong_thuong):
        self.ten_san_pham = ten_san_pham
        self.so_luong = so_luong
        self.gia_thong_thuong = gia_thong_thuong

    def get_price(self, so_luong_mua):
        if so_luong_mua > self.so_luong:
            raise ValueError("Không đủ hàng trong kho.")
        
        # Tính giá dựa vào số lượng mua
        if so_luong_mua < 10:
            return so_luong_mua * self.gia_thong_thuong
        elif 10 <= so_luong_mua < 100:
            return so_luong_mua * self.gia_thong_thuong * 0.9 
        else:
            return so_luong_mua * self.gia_thong_thuong * 0.8 

    def make_purchase(self, so_luong_mua):
        if so_luong_mua > self.so_luong:
            raise ValueError("Không đủ hàng trong kho.")
        
        self.so_luong -= so_luong_mua