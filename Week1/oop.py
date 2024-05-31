# Thêm danh sách học sinh
# Thêm học sinh
# Check dung lượng list

class Treval():
    def __init__(self, n):
        self.n = n
        self.list = []
    def check_list(self):
        if self.n - len(self.list) == 0:
            return False
        else:
            return True
    def add_list(self, name):
        if self.check_list():
            self.list.append(name)
            print(f"Add student {name} Succsecc!")
        else:
            print(f"Add student {name} Error!")

n = 3
treval = Treval(n)
student = ["Tuan", "Hai", "Huy", "Nhân"]
for i in range(len(student)):
    treval.add_list(student[i])

