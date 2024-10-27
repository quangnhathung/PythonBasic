# Một cửa hàng tính phí 12 USD cho mỗi mặt hàng nếu bạn mua ít hơn 10 mặt hàng.
# Nếu bạn mua từ 10 đến 99 các mặt hàng, chi phí là $10 cho mỗi mặt hàng. 
# Nếu bạn mua 100 món trở lên, giá là 7$ một món. 
# #Viết một chương trình hỏi người dùng họ đang mua bao nhiêu mặt hàng và in tổng chi phí.
def Cosst(c):
    if c < 10: 
        return 12
    elif c >= 10 and c<99:  
        return 10
    else: 
        return 7 
        

if __name__ == "__main__":
    a = int (input ("So luong mat hang: "));
    print("Cost: {}$".format(Cosst(a)*a));