# Tính tổng các số lẻ (s = 1+3+5+…+n)
def tong(n):
    if n==0: return 0
    if n%2 != 0: return n+tong(n-1)
    else: return 0+tong(n-1)

print (tong(int(input("Nhap n: "))))