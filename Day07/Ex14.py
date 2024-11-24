# Bài 14: Tìm tất cả các số trong đoạn văn: Sử dụng hàm re.findall và một pattern phù hợp
# để tìm tất cả các số trong đoạn văn, bao gồm cả số nguyên và số thực.
import re
s = "Python là một ngôn ngữ lập trình mạnh mẽ và linh hoạt. Nó hỗ trợ nhiều kiểu dữ liệu khác nhau, trong đó số nguyên (integer) và số thực (float) được sử dụng rất phổ biến. Số nguyên biểu diễn các giá trị không có phần thập phân, ví dụ: 10 or -5, trong khi số thực dùng để biểu diễn các giá trị có phần thập phân như 3.14 hoặc -2.5. Python cung cấp các phép toán cơ bản như cộng, trừ, nhân, chia, giúp lập trình viên dễ dàng xử lý dữ liệu số trong các bài toán hàng ngày."
print (re.findall(r'-?[1-9]+.?\d*',s))