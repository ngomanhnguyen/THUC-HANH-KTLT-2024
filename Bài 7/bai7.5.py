def append_and_read_file(file_path, text_to_append):
    try:
        # Mở file và thêm văn bản (chế độ 'a' để ghi thêm)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text_to_append + '\n')  # Ghi văn bản và xuống dòng

        # Mở lại file và đọc toàn bộ nội dung
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Hiển thị nội dung file
        print("Nội dung tệp sau khi thêm:")
        print(content)

    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Chạy chương trình
if __name__ == "__main__":
    file_path = input("Nhập đường dẫn file: ")
    text_to_append = input("Nhập văn bản muốn thêm: ")
    append_and_read_file(file_path, text_to_append)
