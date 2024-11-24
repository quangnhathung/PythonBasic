# Bài 6: Tìm tất cả các từ chứa một chữ cái 'a': Sử dụng hàm re.findall và một pattern phù hợp 
# để tìm tất cả các từ trong đoạn văn chứa ít nhất một chữ cái 'a'.

import re
s = "English is a West Germanic language in the Indo-European language family, whose speakers, called Anglophones, originated in early medieval England on the island of Great Britain."
print (re.findall(r'\b\w*a\w*\b',s))