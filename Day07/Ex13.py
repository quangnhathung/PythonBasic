# Bài 13: Tách các câu từ đoạn văn: Sử dụng hàm re.split để phân tách đoạn văn thành các câu. 
# Điều này có thể được thực hiện bằng cách sử dụng một pattern phù hợp để tách đoạn văn tại 
# các dấu chấm, dấu phẩy, dấu chấm than, hoặc dấu chấm hỏi.

import re
s = "English is a QUANG West Germanic language in the Indo-European language family, whose speakers, called Anglophones NHAT, originated in early medieval England on the island of Great Britain HUNG."
print (re.split(r'\s',s))