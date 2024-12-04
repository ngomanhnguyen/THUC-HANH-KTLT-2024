import turtle

# Tạo cửa sổ và thiết lập màu nền
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tạo một đối tượng turtle
painter = turtle.Turtle()
painter.fillcolor('blue')  # Màu tô
painter.pencolor('blue')   # Màu bút vẽ
painter.pensize(3)         # Kích thước nét vẽ

# Hàm vẽ hình vuông
def drawsq(t, s):
    for i in range(4):
        t.forward(s)  # Di chuyển về phía trước một khoảng 's'
        t.left(90)    # Xoay trái 90 độ

# Vẽ nhiều hình vuông quay tròn
for i in range(1, 180):
    painter.left(18)            # Xoay trái 18 độ
    drawsq(painter, 200)        # Vẽ hình vuông với cạnh dài 200

# Dừng cửa sổ
window.mainloop()
