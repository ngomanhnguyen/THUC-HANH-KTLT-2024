import math

# Khởi tạo vị trí ban đầu của robot
pos = [0, 0]

# Vòng lặp nhập liệu và xử lý hướng đi
while True:
    s = input("Nhap khoang cach")
    
    if not s:  # Nếu không nhập gì thì thoát vòng lặp
        break
    
    movement = s.split(" ")  # Tách hướng và số bước
    direction = movement[0]  # Hướng đi
    steps = int(movement[1])  # Số bước đi
    
    # Cập nhật vị trí của robot dựa trên hướng đi
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        print("Hướng không hợp lệ!")
        continue

# Tính toán khoảng cách từ vị trí hiện tại về vị trí ban đầu (0,0)
distance = math.sqrt(pos[0]**2 + pos[1]**2)

# In ra khoảng cách là số nguyên gần nhất
print("Khoảng cách từ vị trí hiện tại đến vị trí ban đầu là:", int(round(distance)))
