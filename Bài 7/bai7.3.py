def read_file(file_path):
    try:
        # Mở file và đọc toàn bộ nội dung
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # Đọc toàn bộ nội dung của file

        # In nội dung file
        print("Nội dung tệp:")
        print(content)

    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Chạy chương trình
if __name__ == "__main__":
    file_path = input("Nhập đường dẫn file: ")
    read_file(file_path)
