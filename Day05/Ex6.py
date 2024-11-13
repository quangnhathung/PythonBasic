# Đọc file json gồm mảng các tam giác, gồm độ dài 3 cạnh [{‘a’: 100, ‘b’: 150, ‘c’: 
# 125}, …]. Hãy đọc file và xác định loại tam giác (thường, vuông, cân, đều) và chu vi,
# diện tích hình tam giá. Ghi kết quả vào file csv. Xử lý lỗi: file input không tồn tài, 
# kiểu dữ liệu không chính xác, không phải tam giác, 
import os
import json
import math
path = os.getcwd() + r"\Day05\Data\dataex6.json"
try:
    with open(path, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print ("Khong thay file!")
    
def triangle_info(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
           Ttype = "Tam giác đều"
        elif a == b or b == c or a == c:
           Ttype = "Tam giác cân"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
           Ttype = "Tam giác vuông"
        else:
           Ttype = "Tam giác thường"

        ChuVi = a + b + c
        s = ChuVi / 2
        DienTich = math.sqrt(s * (s - a) * (s - b) * (s - c))

        return {
            "info": f"{a} {b} {c}",
            "Loại":Ttype,
            "ChuVi": ChuVi,
            "DiệnTích": DienTich
        }
    else:
        return {"triangl_type" :"Không phải tam giác hợp lệ"}
try:
    with open(os.getcwd()+ r"\Day05\output\Ex6_classwork.json","w",encoding = "utf-8",newline="") as file:
        l = []
        for i in data:
            x = ["a","b","c"]
            x = dict.fromkeys(x)
            a = triangle_info(int(i["a"]),int(i["b"]),int(i["c"]))
            l.append(a)
        json.dump(l,file,ensure_ascii= False, indent = 4)
            
except FileNotFoundError:
    print ("Khong thay file!")
