print("Ngo Manh Nguyen MSSV: 235752021610058")
def dem_so_dong(ten_tep):
    """Hàm đếm số dòng trong một file

    Args:
        ten_tep (str): Đường dẫn đến file

    Returns:
        int: Số dòng trong file, hoặc 0 nếu file không tồn tại
    """

    try:
        with open(ten_tep, 'r', encoding='utf-8') as file:
            so_dong = 0
            for _ in file:
                so_dong += 1
            return so_dong
    except FileNotFoundError:
        print(f"Tệp {ten_tep} không tồn tại!")
        return 0

# Ví dụ sử dụng
ten_tep = "D:/THỰC HÀNH LẬP TRÌNH/Bài 7/bai7.1.py"
so_dong = dem_so_dong(ten_tep)
if so_dong > 0:
    print(f"Số dòng trong tệp {ten_tep} là: {so_dong}")
