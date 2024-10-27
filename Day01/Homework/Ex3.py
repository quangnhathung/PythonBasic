#Tính tích các số lẻ (tich = 1x3x5x…x n)

def tich(n):
    if n==0: return 0
    if n%2 != 0: return n+tich(n-1)
    else: return 0+tich(n-1)

print (tich(int(input("Nhap n: "))))