print("Ngo Manh Nguyen MSSV: 235752021610058")
def analyze_file(file_path):
    try:
        # Mở file và đọc nội dung
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Đọc tất cả các dòng trong file

        # Tính số dòng
        line_count = len(lines)

        # Tính số ký tự và số từ
        char_count = sum(len(line) for line in lines)  # Tổng số ký tự
        word_count = sum(len(line.split()) for line in lines)  # Tổng số từ

        # In kết quả
        print(f"Phân tích file: {file_path}")
        print(f"Số dòng: {line_count}")
        print(f"Số ký tự: {char_count}")
        print(f"Số từ: {word_count}")

    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Chạy chương trình
if __name__ == "__main__":
    file_path = input("Nhập đường dẫn file: ")
    analyze_file(file_path)
KTDK&TDH
