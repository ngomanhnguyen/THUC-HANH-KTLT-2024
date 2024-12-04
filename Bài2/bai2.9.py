# Nhập chuỗi từ bàn phím
input_string = input("Nhập vào một chuỗi: ")

# Tạo từ điển để lưu số lần xuất hiện của mỗi ký tự
char_count = {}

# Duyệt qua từng ký tự trong chuỗi
for char in input_string:
    if char in char_count:
        char_count[char] += 1  # Nếu ký tự đã có trong từ điển, tăng số đếm
    else:
        char_count[char] = 1   # Nếu ký tự chưa có, thêm vào từ điển với giá trị 1

# In ra từ điển chứa các ký tự và số lần xuất hiện
print(char_count)
