def read_n_lines(file_path, n):
    try:
        # Mở file và đọc nội dung
        with open(file_path, 'r', encoding='utf-8') as file:
            # Đọc n dòng đầu tiên
            lines = [file.readline().strip() for _ in range(n)]

        # In n dòng đầu tiên
        print(f"{n} dòng đầu tiên của file:")
        for line in lines:
            if line:  # In dòng nếu không rỗng
                print(line)
            else:
                break

    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Chạy chương trình
if __name__ == "__main__":
    file_path = input("Nhập đường dẫn file: ")
    n = int(input("Nhập số dòng muốn đọc: "))
    read_n_lines(file_path, n)
