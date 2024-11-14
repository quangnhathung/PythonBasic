# Bài 7. Mô Phỏng Ném Xúc Xắc: Viết một chương trình mô phỏng việc ném xúc xắc. Chương 
# trình sẽ phát sinh ngẫu nhiên giá trị từ 1 đến 6 cho hai xúc xắc và tính tổng của chúng.
import os
import time
import random

os.system("cls")
print("Chương trình ĐỖ THÁNH:")
for x in range(20):
    i = random.randint(1,6)
    j = random.randint(1,6)
    print (f"\rXÚC XẮC: |{i}| |{j}|", end = "")
    time.sleep(0.02)
