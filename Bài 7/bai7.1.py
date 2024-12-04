def read_and_reverse_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Đọc nội dung từ file
            content = file.readlines()
        
        # Đảo ngược nội dung và in ra
        print("Nội dung tệp theo thứ tự ngược lại:")
        for line in reversed(content):
            print(line.strip())
    
    except FileNotFoundError:
        print(f"Tệp '{file_path}' không tồn tại. Vui lòng kiểm tra lại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn tới file
file_path = input("Nhập đường dẫn tới tệp: ")

# Gọi hàm
read_and_reverse_file(file_path)
