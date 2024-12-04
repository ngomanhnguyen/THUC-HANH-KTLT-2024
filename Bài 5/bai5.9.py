print("Ngo Manh Nguuyen MSSV:235752021610058")
from search_module import binary_search

# Chương trình chính
n = int(input("Nhập số lượng phần tử của danh sách: "))
lst = []

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    lst.append(value)

# Sắp xếp danh sách trước khi tìm kiếm
lst.sort()
print("Danh sách sau khi sắp xếp:", lst)

# Nhập giá trị cần tìm
search_value = int(input("Nhập giá trị cần tìm: "))

# Gọi hàm binary_search
position = binary_search(lst, search_value)

if position != -1:
    print(f"Phần tử {search_value} được tìm thấy tại vị trí (index): {position}")
else:
    print(f"Phần tử {search_value} không có trong danh sách.")
