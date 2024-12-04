print("Ngo Manh Nguyen MSSV: 235752021610058")
from utils import sort_list, find_max, find_min

def main():
    try:
        n = int(input("Nhập số lượng phần tử của danh sách: "))
        if n <= 0:
            print("Số lượng phần tử phải lớn hơn 0.")
            return
        
        lst = []
        for i in range(n):
            val = float(input(f"Nhập phần tử thứ {i + 1}: "))
            lst.append(val)
        
        # Gọi module xử lý
        sorted_lst = sort_list(lst)
        max_value = find_max(lst)
        min_value = find_min(lst)
        
        # In kết quả
        print(f"Danh sách sau khi sắp xếp: {sorted_lst}")
        print(f"Phần tử lớn nhất: {max_value}")
        print(f"Phần tử nhỏ nhất: {min_value}")
    except ValueError:
        print("Vui lòng nhập giá trị hợp lệ.")

if __name__ == "__main__":
    main()
