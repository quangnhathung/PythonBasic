# Bài 10: Tìm tất cả các từ kết thúc bằng một số: Sử dụng hàm re.findall và một pattern phù 
# hợp để tìm tất cả các từ trong đoạn văn kết thúc bằng một số

import re
s = "English is2 a West Germanic1 language in the2 Indo-European 2language family, whose  5 speakers, called Anglophones, originated in early medieval England on the island of Great Britain."
print (re.findall(r'\w+\d',s))