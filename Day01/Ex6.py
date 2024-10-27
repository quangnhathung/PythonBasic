# Viết chương trình tính tổng các số 
# từ 0 đến 999 mà là bội của 3 hoặc 5.
a= [i for i in range(0,999) if i%3 ==0 and i%5==0]
print (sum(a))