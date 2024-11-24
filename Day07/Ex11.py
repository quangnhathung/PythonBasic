# Bài 11: Tìm tất cả các từ có độ dài ít nhất 5 ký tự: Sử dụng hàm re.findall và một pattern 
# phù hợp để tìm tất cả các từ trong đoạn văn có độ dài ít nhất là 5 ký tự.
import re
s = "English is a West Germanic language in the Indo-European language family, whose speakers, called Anglophones, originated in early medieval England on the island of Great Britain."
print (re.findall(r'\w{5,}',s))