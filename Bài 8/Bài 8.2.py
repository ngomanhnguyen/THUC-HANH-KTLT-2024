print("Ngo Manh Nguyen MSSV:235752021610058")
import turtle, random

# Danh sách màu sắc
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Tạo đối tượng Turtle
painter = turtle.Turtle()
painter.pensize(3)  # Đặt độ dày nét vẽ

# Vòng lặp vẽ 10 hình
for i in range(10):
    color = random.choice(colors)       # Chọn màu ngẫu nhiên từ danh sách
    painter.pencolor(color)            # Đặt màu bút vẽ
    painter.circle(100)                # Vẽ hình tròn bán kính 100
    painter.right(30)                  # Quay phải 30 độ
    painter.left(60)                   # Quay trái 60 độ
    painter.setposition(0, 0)          # Đặt vị trí con trỏ về tâm (0, 0)
