# Bài 3. Quản Lý Danh Sách Công Việc:
#  Xây dựng một ứng dụng quản lý danh sách công việc với các thao tác CRUD.
#  Mỗi công việc sẽ có các thuộc tính như tiêu đề, mô tả, ngày bắt đầu, ngày kết thúc, 
# trạng thái (hoàn thành/chưa hoàn thành), v.v.
#  Dữ liệu ban đầu sẽ được tạo ngẫu nhiên với một danh sách các công việc.
#  Người dùng có thể thêm mới, xem danh sách, cập nhật thông tin và xóa công việc khỏi 
# danh sách.
#  Dữ liệu sẽ được lưu trữ trong một tệp JSON.
import json
from random import choice, randint
from datetime import datetime, timedelta
from os import getcwd

# Danh sách công việc ngẫu nhiên
titles = [
    "Quản lý dự án", "Lập kế hoạch chiến lược", "Phân tích dữ liệu", "Thiết kế giao diện người dùng",
    "Phát triển phần mềm", "Kiểm thử phần mềm", "Tạo nội dung tiếp thị", "Quản lý mạng xã hội",
    "Hỗ trợ khách hàng", "Viết bài blog", "Quản lý tài chính", "Tổ chức sự kiện", 
    "Lập báo cáo tài chính", "Giải quyết tranh chấp", "Quản lý nhân sự", "Lập kế hoạch sản phẩm",
    "Đào tạo nhân viên", "Giám sát sản xuất", "Phân tích thị trường", "Quản lý kho",
    "Tạo mẫu sản phẩm", "Chạy chiến dịch quảng cáo", "Tư vấn bán hàng", "Phân phối sản phẩm",
    "Quản lý hợp đồng", "Lên kế hoạch tài trợ", "Nghiên cứu xu hướng ngành", "Đảm bảo chất lượng",
    "Phân tích hiệu suất", "Xây dựng mối quan hệ đối tác"
]

descriptions = [
    "Mô tả công việc quản lý dự án", "Mô tả công việc lập kế hoạch chiến lược", "Mô tả công việc phân tích dữ liệu",
    "Mô tả công việc thiết kế giao diện", "Mô tả công việc phát triển phần mềm", "Mô tả công việc kiểm thử phần mềm",
    "Mô tả công việc tạo nội dung tiếp thị", "Mô tả công việc quản lý mạng xã hội", "Mô tả công việc hỗ trợ khách hàng",
    "Mô tả công việc viết bài blog", "Mô tả công việc quản lý tài chính", "Mô tả công việc tổ chức sự kiện",
    "Mô tả công việc lập báo cáo tài chính", "Mô tả công việc giải quyết tranh chấp", "Mô tả công việc quản lý nhân sự",
    "Mô tả công việc lập kế hoạch sản phẩm", "Mô tả công việc đào tạo nhân viên", "Mô tả công việc giám sát sản xuất",
    "Mô tả công việc phân tích thị trường", "Mô tả công việc quản lý kho", "Mô tả công việc tạo mẫu sản phẩm",
    "Mô tả công việc chạy chiến dịch quảng cáo", "Mô tả công việc tư vấn bán hàng", "Mô tả công việc phân phối sản phẩm",
    "Mô tả công việc quản lý hợp đồng", "Mô tả công việc lên kế hoạch tài trợ", "Mô tả công việc nghiên cứu xu hướng",
    "Mô tả công việc đảm bảo chất lượng", "Mô tả công việc phân tích hiệu suất", "Mô tả công việc xây dựng mối quan hệ"
]

class Task:
    def __init__(self, title, description, start_date, end_date, status):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __str__(self):
        return f"Tiêu đề: {self.title}, Mô tả: {self.description}, Ngày bắt đầu: {self.start_date}, Ngày kết thúc: {self.end_date}, Trạng thái: {self.status}"

class Task_Manager:
    def __init__(self):
        self.list = []

    def add(self, a):
        self.list.append(a)
    
    def read(self):
        if not self.list:
            print("Danh sách công việc trống.")
        else:
            print("Danh sách công việc:")
            for task in self.list:
                print(task)

    def update(self, title, new_title=None, new_description=None, new_start_date=None, new_end_date=None, new_status=None):
        found = False
        for task in self.list:
            if task.title == title:
                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description
                if new_start_date:
                    task.start_date = new_start_date
                if new_end_date:
                    task.end_date = new_end_date
                if new_status:
                    task.status = new_status
                found = True
                break
        if not found:
            print(f"Không tìm thấy công việc có tiêu đề: {title}")
            
    def delete(self, title):
        initial_len = len(self.list)
        self.list = [task for task in self.list if task.title != title]
        if len(self.list) < initial_len:
            print(f"Đã xóa công việc có tiêu đề: {title}")
        else:
            print(f"Không tìm thấy công việc có tiêu đề: {title}")


def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = randint(0, delta.days)
    return start_date + timedelta(days=random_days)


if __name__ == "__main__":
    manager = Task_Manager()
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    statuses = ["Hoàn thành", "Chưa hoàn thành"]
    
    for _ in range(30):
        task = Task(
            choice(titles), 
            choice(descriptions), 
            random_date(start_date, end_date).strftime("%Y-%m-%d"), 
            random_date(start_date, end_date).strftime("%Y-%m-%d"), 
            choice(statuses)
        )
        manager.add(task)

    try:
        path = getcwd() + r"\Day06\output\Ex3_homework.json"
        key = ["Tiêu đề", "Mô tả", "Ngày bắt đầu", "Ngày kết thúc", "Trạng thái"]
        data = []
        for t in manager.list:
            dic = dict.fromkeys(key, None)
            dic["Tiêu đề"] = t.title
            dic["Mô tả"] = t.description
            dic["Ngày bắt đầu"] = t.start_date
            dic["Ngày kết thúc"] = t.end_date
            dic["Trạng thái"] = t.status
            data.append(dic)
        
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    except FileNotFoundError:
        print("Không tìm thấy file")
