# Bài 9: Tìm tất cả các từ bắt đầu bằng một chữ cái in hoa: Sử dụng hàm re.findall và một 
# pattern phù hợp để tìm tất cả các từ trong đoạn văn bắt đầu bằng một chữ cái in hoa.

import re
s = "English is a West Germanic language in the Indo-European language family, whose speakers, called Anglophones, originated in early medieval England on the island of Great Britain."
print (re.findall(r'[A-Z]\w*',s))