# Bài 2. Quản Lý Danh Sách Sản Phẩm:
#  Xây dựng một ứng dụng quản lý danh sách sản phẩm với các thao tác CRUD.
#  Sản phẩm sẽ được mô tả bởi các thuộc tính như tên, mô tả, giá, số lượng, v.v.
#  Dữ liệu ban đầu sẽ được tạo ngẫu nhiên với một danh sách các sản phẩm.
#  Người dùng có thể thêm mới, xem danh sách, cập nhật thông tin và xóa sản phẩm khỏi 
# danh sách.
#  Dữ liệu sẽ được lưu trữ trong một tệp JSON.

import json
from random import choice
from os import getcwd

names = [
    "Sản phẩm A", "Sản phẩm B", "Sản phẩm C", "Sản phẩm D", "Sản phẩm E",
    "Sản phẩm F", "Sản phẩm G", "Sản phẩm H", "Sản phẩm I", "Sản phẩm J",
    "Sản phẩm K", "Sản phẩm L", "Sản phẩm M", "Sản phẩm N", "Sản phẩm O",
    "Sản phẩm P", "Sản phẩm Q", "Sản phẩm R", "Sản phẩm S", "Sản phẩm T",
    "Sản phẩm U", "Sản phẩm V", "Sản phẩm W", "Sản phẩm X", "Sản phẩm Y",
    "Sản phẩm Z", "Sản phẩm AA", "Sản phẩm AB", "Sản phẩm AC", "Sản phẩm AD"
]

descriptions = [
    "Mô tả sản phẩm A", "Mô tả sản phẩm B", "Mô tả sản phẩm C", "Mô tả sản phẩm D", "Mô tả sản phẩm E",
    "Mô tả sản phẩm F", "Mô tả sản phẩm G", "Mô tả sản phẩm H", "Mô tả sản phẩm I", "Mô tả sản phẩm J",
    "Mô tả sản phẩm K", "Mô tả sản phẩm L", "Mô tả sản phẩm M", "Mô tả sản phẩm N", "Mô tả sản phẩm O",
    "Mô tả sản phẩm P", "Mô tả sản phẩm Q", "Mô tả sản phẩm R", "Mô tả sản phẩm S", "Mô tả sản phẩm T",
    "Mô tả sản phẩm U", "Mô tả sản phẩm V", "Mô tả sản phẩm W", "Mô tả sản phẩm X", "Mô tả sản phẩm Y",
    "Mô tả sản phẩm Z", "Mô tả sản phẩm AA", "Mô tả sản phẩm AB", "Mô tả sản phẩm AC", "Mô tả sản phẩm AD"
]

prices = [
    1000, 1200, 1500, 2000, 2500,
    3000, 3500, 4000, 4500, 5000,
    1800, 1300, 1700, 2600, 3400,
    2100, 3900, 4100, 2900, 2700,
    3100, 3200, 3300, 3700, 3800,
    4200, 4400, 4600, 4700, 4900
]

quantities = [
    10, 20, 15, 30, 25,
    40, 35, 50, 45, 60,
    18, 13, 17, 26, 34,
    21, 39, 41, 29, 27,
    31, 32, 33, 37, 38,
    42, 44, 46, 47, 49
]

# Lớp Sản phẩm
class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Tên: {self.name}, Mô tả: {self.description}, Giá: {self.price}, Số lượng: {self.quantity}"

# Quản lý danh sách sản phẩm
class Product_Manager:
    def __init__(self):
        self.list = []

    def add(self, a):
        self.list.append(a)
    
    def read(self):
        if not self.list:
            print("Danh sách trống.")
        else:
            print("Danh sách sản phẩm:")
            for product in self.list:
                print(product)

    def update(self, name, new_name=None, new_description=None, new_price=None, new_quantity=None):
        found = False
        for product in self.list:
            if product.name == name:
                if new_name:
                    product.name = new_name
                if new_description:
                    product.description = new_description
                if new_price is not None:
                    product.price = new_price
                if new_quantity is not None:
                    product.quantity = new_quantity
                found = True
                break
        if not found:
            print(f"Không tìm thấy sản phẩm có tên: {name}")
            
    def delete(self, name):
        initial_len = len(self.list)
        self.list = [product for product in self.list if product.name != name]
        if len(self.list) < initial_len:
            print(f"Đã xóa sản phẩm có tên: {name}")
        else:
            print(f"Không tìm thấy sản phẩm có tên: {name}")

# Chạy chương trình
if __name__ == "__main__":
    manager = Product_Manager()
    for _ in range(100):
        product = Product(choice(names), choice(descriptions), choice(prices), choice(quantities))
        manager.add(product)

    try:
        path = getcwd() + r"\Day06\output\Ex2_homework.json"
        key = ["Tên", "Mô tả", "Giá", "Số lượng"]
        data = []
        for p in manager.list:
            dic = dict.fromkeys(key, None)
            dic["Tên"] = p.name
            dic["Mô tả"] = p.description
            dic["Giá"] = p.price
            dic["Số lượng"] = p.quantity
            data.append(dic)
        
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    except FileNotFoundError:
        print("Không tìm thấy tệp.")
