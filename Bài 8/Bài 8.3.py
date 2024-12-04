print("Ngo Manh Nguyen MSSV: 235752021610058")
import turtle
import random

# Tạo danh sách màu sắc
colors = ["red", "green", "blue"]

# Tạo đối tượng Turtle
painter = turtle.Turtle()
painter.pensize(2)  # Đặt kích thước nét vẽ
painter.speed(0)    # Tăng tốc độ vẽ tối đa

# Hàm vẽ các hình tròn lồng nhau
def draw_circles():
    for i in range(12):  # Vẽ 12 hình tròn, mỗi hình quay 30 độ
        color = random.choice(colors)  # Lấy màu ngẫu nhiên từ danh sách
        painter.pencolor(color)        # Đặt màu bút vẽ
        painter.circle(100)            # Vẽ đường tròn bán kính 100
        painter.right(30)              # Quay 30 độ cho lần lặp tiếp theo

# Thực hiện vẽ
draw_circles()

# Kết thúc vẽ
painter.hideturtle()  # Ẩn con trỏ vẽ
turtle.done()
