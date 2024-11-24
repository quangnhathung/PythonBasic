# Bài 12: Tìm tất cả các từ được viết hoa trong đoạn văn: Sử dụng hàm re.findall và
# một pattern phù hợp để tìm tất cả các từ trong đoạn văn được viết hoa (tất cả các
# ký tự trong từ đều là chữcái in hoa).
import re
s = "English is a QUANG West Germanic language in the Indo-European language family, whose speakers, called Anglophones NHAT, originated in early medieval England on the island of Great Britain HUNG."
print (re.findall(r'\b[A-Z]+\b',s))