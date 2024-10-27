# Tính n! (n giai thừa)
def fractor(n):
    if n==1: return 1
    return n*fractor(n-1);

a= int (input("Nhap n: "))
b= fractor(a);
print(f'{a}! = {b}')