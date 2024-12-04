print("Ngo Manh Nguyen MSSV: 235751610058")
def write_list_to_file(file_name, data_list):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"Nội dung đã được ghi vào tệp '{file_name}' thành công.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi ghi tệp: {e}")

# Ví dụ sử dụng
my_list = ["Python", "Lập trình", "Ghi dữ liệu vào tệp", "Danh sách"]
file_name = "D:/THỰC HÀNH LẬP TRÌNH/Bài 7/bai7.1.py"

write_list_to_file(file_name, my_list)
