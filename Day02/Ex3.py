# Cho mảng 2 chiều a có m dòng, n cột chứa số nguyên, viết các hàm sau: 
# a. Tạo mảng a chứa các số nguyên ngẫu nhiên. 
# b. Xuất các phần tử thuộc dòng k. 
# c. Xuất các phần tử thuộc cột k. 
# d. Tìm dòng có tổng lớn nhất. 
# e. Tìm cột có tích nhỏ nhất. 
# f. Xuất ra các phần tử thuộc dòng chẵn và cột lẻ trong a. 
# g. Tính trung bình cộng các phần tử chẵn thuộc dòng lẻ của a. 
# h. Tính trung bình cộng các phần tử thuộc biên. 
# i. Tính trung bình tích các phần tử không thuộc biên. 

from random import randint
def init():
    n,m = map(int, input("Nhap hang va cot: ").split())
    list2d = [[randint(-99,100) for i in range(m)] for j in range(n)]
    return list2d,n,m
def printlist(list2d):
    for i in list2d:
        for j in i:
            print("{:>4}".format(j), end = "")
        print()
def printrow(list2d,k):
    for i in list2d[k-1]:
        print("{:>4}".format(i),end = "")
def printcol(list2d, col):
    for i in list2d:
        print("{:>4}".format(i[col-1]),end="")

# d. Tìm dòng có tổng lớn nhất
def Sumax(list2d,n,m):
    sum = [0 for i in range(0,n)]
    for i in range(n):
        for j in range(0,m):
            sum[i] += list2d[i][j]
    pos = sum.index(max(sum))
    return pos + 1
# e. Tìm cột có tích nhỏ nhất. 
def MultiplicationMin(list2d,n,m):
    multiplication = [0 for i in range(0,n)]
    for i in range(n):
        for j in range(0,m):
            multiplication[i] *= list2d[i][j]
    pos = multiplication.index(min(multiplication))
    return pos + 1
# f. Xuất ra các phần tử thuộc dòng chẵn và cột lẻ trong a. 
# g. Tính trung bình cộng các phần tử chẵn thuộc dòng lẻ của a. 
# h. Tính trung bình cộng các phần tử thuộc biên. 
# i. Tính trung bình tích các phần tử không thuộc biên. 
def f_func(list2d,n,m):
    for i in range(n):
        if i%2 !=0: continue;
        for j in range(0,m):
            if j % 2 != 0:
                print(i,end= "")
def g_func(list2d,n,m):
    average=0
    for i in range(n):
        if i%2 == 0: continue;
        for j in range(0,m):
            if list2d[i][j] % 2 == 0:
                average+=list2d[i][j]
    return average/m
def h_func(list2d,n,m):
    sum=0
    for i in range(n):
        for j in range(0,m):
            if i == 0 or i == n-1 or j == 0 or j == m-1: 
                sum += list2d[i][j]
    return sum
def i_func(list2d,n,m):
    sum=0
    for i in range(n):
        for j in range(0,m):
            if i == 0 or i == n-1 or j == 0 or j == m-1: 
                sum += list2d[i][j]
    sum1=0
    for i in range(n):
        for j in range(0,m):
                sum += list2d[i][j]
    return sum1-sum

def menu():
    print("Menu lựa chọn bài tập:")
    print("0. Thoát chương trình.")
    print("1. Xuất các phần tử thuộc dòng k.")
    print("2. Xuất các phần tử thuộc cột k.")
    print("3. Tìm dòng có tổng lớn nhất.")
    print("4. Tìm cột có tích nhỏ nhất.")
    print("5. Xuất ra các phần tử thuộc dòng chẵn và cột lẻ.")
    print("6. Tính trung bình cộng các phần tử chẵn thuộc dòng lẻ.")
    print("7. Tính tổng các phần tử thuộc biên.")
    print("8. Tính tổng các phần tử không thuộc biên.")
    print("0. Thoát chương trình.")
    
    choice = int(input("Vui lòng chọn một bài tập (0-8): "))
    return choice

if __name__ == "__main__":
    list2d,n,m = init()
    printlist(list2d)
    print()
    while 1:
        choice = menu()
        if choice == 1:
            k = int(input("Dòng thứ mấy: "))
            printrow(list2d,k)
        elif choice == 2: 
            k = int(input("Cột thứ mấy: "))
            printcol(list2d,k)
        elif choice == 3:
            print(Sumax(list2d,n,m))
        elif choice == 4:
            print(MultiplicationMin(list2d,n,m))
        elif choice == 5:
            f_func(list2d,n,m)
        elif choice == 5:
            g_func(list2d,n,m)
        elif choice == 7:
            print(h_func(list2d,m,n))
        elif choice == 8:
            print(i_func(list2d,n,m))
