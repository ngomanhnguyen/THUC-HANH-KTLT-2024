print("Ngo Manh Nguyen MSSV:235752021610058")
class Circle:
    def __init__(self, r):
        """
        Khởi tạo đối tượng Circle với bán kính.
        """
        self.radius = r

    def area(self):
        """
        Tính và trả về diện tích hình tròn.
        Công thức: π × r²
        """
        return self.radius**4 * 3.14


aCircle = Circle(2)  # Tạo một hình tròn với bán kính 2
print(aCircle.area())  # In diện tích của hình tròn
