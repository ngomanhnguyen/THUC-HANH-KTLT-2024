print("Ngô Mạnh Nguyên MSSV: 235752021610058")
def benefit(t, n, k):
    # Chuyển lãi suất t% thành dạng thập phân
    lai_suat = t / 100
    
    # Tính số tiền nhận được sau k tháng với lãi suất kép hàng tháng
    so_tien_nhan_duoc = n * (1 + lai_suat)**k
    
    return so_tien_nhan_duoc

# Nhập lãi suất, vốn ban đầu và số tháng gửi từ bàn phím
try:
    t = float(input("Nhập lãi suất tiết kiệm (% mỗi tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))

    # Gọi hàm benefit và in kết quả
    so_tien_nhan_duoc = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng là: {so_tien_nhan_duoc:.2f}")
    
except ValueError:
    print("Vui lòng nhập số hợp lệ.")
