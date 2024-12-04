print("Ngô Mạnh Nguyên MSSV:235752021610058")
import math

def Tinh(R):
    # Kiểm tra giá trị bán kính phải là một số dương
    if R <= 0:
        return "Bán kính không hợp lệ. Vui lòng nhập một số dương."

    # Tính chu vi (C = 2 * pi * R)
    chu_vi = 2 * math.pi * R

    # Tính diện tích (A = pi * R^2)
    dien_tich = math.pi * R**2

    # Trả về chu vi và diện tích
    return f"Chu vi hình tròn là: {chu_vi:.2f}\nDiện tích hình tròn là: {dien_tich:.2f}"

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính hình tròn: "))
    # Gọi hàm Tinh và in kết quả
    print(Tinh(R))
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
