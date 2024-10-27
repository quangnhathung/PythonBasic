# Trong học chế tín chỉ, thang điểm đánh giá được chia thành điểm không đạt và điểm đạt.
#  Điểm không đạt: 0 - 3,9 thang điểm 10 tương đương điểm F= 0 thang điểm 4.
#  Điểm đạt:
#  4,0 -5,4 thang điểm 10 tương đương điểm D =1 thang điểm 4.
#  5,5 -6,9 thang điểm 10 tương đương điểm C= 2 thang điểm 4.
#  7,0 -8,4 thang điểm 10 tương đương điểm B =3 thang điểm 4.
#  8,5 - 10 thang điểm 10 tương đương điểm A= 4 thang điểm 4.


def Sorce(c):
    if c < 4: 
        return "Không đạt. Điểm F"
    elif c > 4 and c < 5.4:  
        return "Đạt. Điểm D"
    elif c > 5.4 and c < 6.9: 
        return "Đạt. Điểm C"
    elif c > 7 and c <= 8.4: 
        return "Đạt. Điểm B"
    elif c >8.4: 
        return "Đạt. Điểm A"

if __name__ == "__main__":
    a = int (input ("Nhap điểm: "));
    print(Sorce(a));