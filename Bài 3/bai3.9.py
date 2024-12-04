print("Ngô Mạnh Nguyên MSSV: 235752021610058")
# Hàm cộng hai số
def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    if y == 0:
        return "Lỗi! Không thể chia cho 0."
    return x / y

# Chương trình chính
def calculator():
    print("Chọn phép toán:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")

    # Người dùng chọn phép toán
    choice = input("Nhập lựa chọn (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Nhập số thứ nhất: "))
        num2 = float(input("Nhập số thứ hai: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Lựa chọn không hợp lệ.")

# Gọi chương trình máy tính
calculator()
