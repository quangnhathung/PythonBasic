# Xóa khoảng trắng thừa ở đầu và cuối chuỗi 
# “ Hello World ”. 
# Chuyển chuỗi sang dạng 
# hoa và thường. 
# Thay ký tự H thành ký tự J.
str= " Hello World "
print ("Xóa khaongr trắng:", str.strip())
print ("Hoa:", str.upper())
print ("Thường:", str.lower())
print ("Hoa->thuowng, thuong -> hoa", str.swapcase())
str1=str.strip().title()
print ("Vì string trong Python là \'unhasble\' nên không thể thay đổi")