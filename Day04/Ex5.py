# Bài 5. Viết một lớp tên là Wordplay. Nó phải có một trường chứa danh sách các từ. Người 
# dùng của lớp phải chuyển danh sách các từ họ muốn sử dụng cho lớp. Cần có các phương 
# thức sau:
# (1) words_with_length(length): trả về danh sách độ dài của tất cả các từ
# (2) started_with(s): trả về danh sách tất cả các từ bắt đầu bằng s
# (3) end_with(s): trả về danh sách tất cả các từ kết thúc bằng s
# (4) only(L): trả về danh sách các từ chỉ chứa các chữ cái đó trong L
# (5) avoids (L): trả về danh sách các từ không chứa chữ cái nào trong L

from os import getcwd
class WorldPlay:
    def __init__(self):
        self.words = []
    
    def add(self,a):
        self.words.extend(a)
    def words_with_length(self,ln):
        l = []
        for i in self.words:
            if len(i) == ln: l.append(i)
        return l
    
    def started_with(self,c):
        l = []
        for i in self.words:
            if (i[0].casefold() == c.casefold()): l.append(i)
        return l
    
    def end_with(self,c):
        l = []
        for i in self.words:
            if (i[len(i)-1] == c): l.append(i)
        return l
    
    def only(self,ch):
        l = []
        for i in self.words:
            if ch in i: l.append(i)
        return l
    def avoids (self,ch):
        l = []
        for i in self.words:
            if ch not in i: l.append(i)
        return l

a= WorldPlay()
path = getcwd() + "\\Day04\\input.txt"
with open(path,"r") as file:
    s = file.read().strip().split()
    a.add(s)

#print(a.words_with_length(0))
#print(a.started_with("d"))
#print(a.end_with("s"))
#print(a.only("ca"))
#print(a.avoids("ca"))