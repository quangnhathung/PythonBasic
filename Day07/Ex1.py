#  Kiểm tra tính hợp lệ của địa chỉ email, số điện thoại, password
# 1. Viết một phương thức Python để kiểm tra xem một chuỗi đầu vào có phải là một địa 
# chỉ email hợp lệ hay không.
# 2. Viết một phương thức Python để kiểm tra xem một chuỗi đầu vào có phải là một số
# điện thoại hợp lệ hay không.
# 3. Viết một phương thức Python để kiểm tra xem một chuỗi đầu vào có phải là một 
# password hợp lệ hay không

from re import *
import os

patern_email = r"[a-z0-9]+@(gmail|edu|yahoo)+.(com|vn)"
patern_phone = r"0\d{9}"
patern_pass = r"[*-9A-Za-z]{8,16}"

while 1:
    print("1. Check password\n2. Check Email\n3. Check Phone number\n option: ",end = "")
    i = int(input().strip())
    os.system("cls")
    if i == 0:break
    elif i == 1:
        if (match(patern_pass, input("Nhap pass: ").strip())):
            print("Valid")
        else: print("Invalid")
    elif i == 2:
        if (match(patern_email, input("Nhap email: ").strip())):
            print("Valid")
        else: print("Invalid")
    elif i == 3:
        if (match(patern_phone, input("Nhap sdt: ").strip())):
            print("Valid")
        else: print("Invalid")