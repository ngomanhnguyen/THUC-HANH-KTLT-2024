print("Ngo Manh Nguyen MSSV:235752021610058")
import math

class Circle:
    def __init__(self, radius):
        """
        Hàm khởi tạo (constructor) cho lớp Circle.
        :param radius: Bán kính của hình tròn (float hoặc int)
        """
        self.radius = radius

    def area(self):
        """
        Tính diện tích của hình tròn.
        :return: Diện tích hình tròn (float)
        """
        return math.pi * self.radius ** 2

    def circumference(self):
        """
        Tính chu vi của hình tròn.
        :return: Chu vi hình tròn (float)
        """
        return 2 * math.pi * self.radius

# Sử dụng lớp Circle
if __name__ == "__main__":
    # Tạo một đối tượng Circle với bán kính 5
    my_circle = Circle(6)

    # Tính diện tích và chu vi
    print(f"Bán kính: {my_circle.radius}")
    print(f"Diện tích: {my_circle.area():.2f}")
    print(f"Chu vi: {my_circle.circumference():.2f}")
