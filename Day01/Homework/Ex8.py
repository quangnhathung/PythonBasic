# Những năm nào chia hết cho 4 được và không chia hết cho 100 được coi là năm nhuận (ví dụ năm 
# 2100 không phải là năm nhuận, 2104 là năm nhuận). Viết chương trình hỏi người dùng một năm và 
# in ra xem đó có phải là năm nhuận hay không.
# Hàm kiểm tra năm nhuận

def Check_yrs(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    year = int(input("Nhập vào một năm: "))

    if Check_yrs(year):
        print(f"Năm {year} là năm nhuận.")
    else:
        print(f"Năm {year} không phải là năm nhuận.")
