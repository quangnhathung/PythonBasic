# Bài 5: Tách từ khỏi đoạn văn: Sử dụng hàm re.findall để tìm tất cả các từ trong đoạn văn. 
# Điều này có thể giúp phân tách đoạn văn thành danh sách các từ.

import re
s = "Bài 5: Tách từ khỏi đoạn văn: Sử dụng hàm re.findall để tìm tất cả cá."
print (re.findall(r"\w+",s))