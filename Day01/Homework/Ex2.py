# Tính tích các số chẵn (tich = 2x4x6x…x n)
def tich(n):
    if n==0: return 1
    if n%2 == 0: return n*tich(n-1)
    else: return 1*tich(n-1)

print (tich(int(input("Nhap n: "))))