print("Ngo Manh Nguyen MSSV: 235752021610058")
class IOString:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Nhập vào một chuỗi: ")

    def print_String(self):
        print(self.str1.upper())

# Tạo đối tượng
str1 = IOString()

# Gọi các phương thức
str1.get_String()
str1.print_String()
