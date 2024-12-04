# Nhập chuỗi các số nhị phân từ người dùng, phân tách bởi dấu phẩy
binary_numbers = input("Nhập các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ").split(",")

# Khởi tạo danh sách để lưu các số nhị phân chia hết cho 5
divisible_by_5 = []

# Duyệt qua từng số nhị phân trong danh sách
for binary in binary_numbers:
    # Chuyển số nhị phân thành số thập phân
    decimal_value = int(binary, 2)
    
    # Kiểm tra nếu số thập phân chia hết cho 5
    if decimal_value % 5 == 0:
        divisible_by_5.append(binary)

# In kết quả, các số chia hết cho 5 cách nhau bởi dấu phẩy
print(",".join(divisible_by_5))
