# Bài 10. Tạo Mật Khẩu Ngẫu Nhiên: Viết một chương trình tạo một mật khẩu ngẫu nhiên 
# bằng cách sử dụng các ký tự chữ cái, số và ký tự đặc biệt từ bộ ký tự ASCII. 
# Chương trình sẽ yêu cầu người dùng nhập độ dài của mật khẩu và tạo một mật khẩu 
# ngẫu nhiên có độ dài đó.

import random
import string

length = 8
all = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all) for i in range(length))

print(password)
