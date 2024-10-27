# Hãy dùng vòng lặp in ra các dấu * theo mẫu:
# Nhập vào chiều rộng và chiều cao. In ra hình chữ nhật đặc/rỗng
# In một hình tam giác vuông. Cho phép người dùng chỉ 
# định mức độ cao hình tam giác:
# In hình thoi như hình bên, cho phép người dùng chỉ định mức 
# độ cao kim cương

def Hinhvuong(n,m):
    for i in range(n):
        for j in range(m):
            print("* ",end="")
        print();
    print()
    for i in range(n):
        for j in range(m):
            if i==0 or i == n-1 or j== 0 or j==m-1:
                print("* ",end="")
            else: print ("  ", end="")
        print();

def Tamgiacvuong(n):
    for i in range(n+1):
        for j in range (i):
            print ("* ", end="")
        print ()
def Thoi(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    
if __name__ == "__main__":
    Hinhvuong(3,4)
    Tamgiacvuong(5)
    Thoi(5)
