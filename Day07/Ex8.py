# Bài 8: Tìm tất cả các dấu câu trong đoạn văn: Sử dụng hàm re.findall và một pattern phù hợp 
# để tìm tất cả các dấu câu (dấu chấm, dấu phẩy, dấu chấm than, dấu chấm hỏi, dấu chấm 
# phẩy, ...) trong đoạn văn.
import re
s = "English is a West Germanic language in the Indo-European language family, whose speakers, called Anglophones, originated in early medieval England on the island of Great Britain."
print (re.findall(r'[^a-zA-Z\s]',s))