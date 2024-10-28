'''Cho mảng 2 chiều a có m dòng, n cột chứa số nguyên, viết các hàm sau: 
a. Tính tổng các phần tử thuộc tam giác trên của đường chéo phụ kể cả 
    đường chéo phụ trong ma trận vuông a cấp n. 
b. Chuyển các phần tử âm thành trị tuyệt đối của nó trong a. 
c. Thay các phần tử chẵn trong a bằng số nguyên x cho trước. 
d. Kiểm tra a có toàn chẵn không? 
e. Cho ma trận vuông a cấp n, viết hàm kiểm tra a có đối xứng không. 
    Biết rằng ma trận đối 
    xứng là ma trận có a[i][j] = a[j][i].
f. Kiểm tra ma trận vuông a cấp n có đường chéo chính tăng dần không? 
g. Xuất các phần tử thuộc tam giác dưới của đường chéo phụ kể cả đường chéo phụ 
    trong ma trận vuông a cấp n. 
h. Kiểm tra ma trận vuông a cấp n có đường chéo phụ giảm dần không'''
from random import randint
from copy import deepcopy
def menu():
    print("Menu lựa chọn bài tập:")
    print("0. Thoát chương trình.")
    print("1. Tính tổng các phần tử thuộc tam giác trên của đường chéo phụ.")
    print("2. Chuyển các phần tử âm thành trị tuyệt đối của nó.")
    print("3. Thay các phần tử chẵn bằng số nguyên x cho trước.")
    print("4. Kiểm tra ma trận có toàn chẵn không?")
    print("5. Kiểm tra ma trận có đối xứng không?")
    print("6. Kiểm tra ma trận có đường chéo chính tăng dần không?")
    print("7. Xuất các phần tử thuộc tam giác dưới của đường chéo phụ.")
    print("8. Kiểm tra ma trận có đường chéo phụ giảm dần không?")
    choice = int(input("Vui lòng chọn một bài tập (0-8): "))
    return choice

def printmtrx(a):
    for i in a:
        for j in i:
            print("{:>4}".format(j),end="")
        print()
    return
        
if __name__ == "__main__":
    n = int(input("Ma tran vuong cap: "))
    matrix = [[randint(-99,99) for i in range(n)] for i in range (n)]
    printmtrx(matrix)
    while 1:
        choice = menu()
        if choice == 0: break;
        elif choice==1:
            sum=0
            for i in range(n):
                for j in range(n-i-1):
                    sum+= matrix[i][j]
            print(sum,end="\n\n")
        elif choice == 2:
            matrix1 = deepcopy(matrix)
            for i in range(n):
                for j in range(n):
                    matrix1[i][j] = abs(matrix1[i][j])
            printmtrx(matrix1)
            print(end=("\n\n"))
            printmtrx(matrix)
        elif choice == 3:
            x = int(input("So: "))
            matrix1 = deepcopy(matrix)
            for i in range(n):
                for j in range(n):
                    if matrix1[i][j] % 2 == 0:
                        matrix1[i][j] = x;
            printmtrx(matrix1)
            print(end=("\n\n"))
            printmtrx(matrix)
        elif choice == 4:
            for i in a:
                for j in i:
                    if (j % 2 != 0):
                        print ("Khong", end="\n\n")
                        break;

        elif choice == 5:
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] != matrix[j][i]:
                        print ("Khong", end="\n\n")
                        break;
        elif choice == 6:
            flag = True;
            for i in range(n-1):
                if matrix[i][i] > matrix[i+1][i+1]:
                    flag = False;
                    break;
            if (flag): print ("Tang dan");
            else: print("khong")
            print()
        elif choice == 7:
            for i in range(1,n):
                for  j in range(n-i,n):
                    print (matrix[i][j],end=" ")
                print()
        elif choice == 8:
            flag = True;
            for i in range(n-1):
                if matrix[i][n-i-1] < matrix[i+1][n-1-1-i] :
                    flag = False
                    break
            if (flag): print ("Giam dan");
            else: print("khong")