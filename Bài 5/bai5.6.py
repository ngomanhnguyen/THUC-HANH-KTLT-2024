print("Ngo Manh Nguyen MSSV:235752021610058")
def sort_list(lst):
    return sorted(lst)

def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

# Nhập danh sách từ bàn phím
n = int(input("Nhập số lượng phần tử của danh sách: "))
lst = []

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    lst.append(value)

# Sắp xếp và tìm giá trị lớn nhất, nhỏ nhất
sorted_list = sort_list(lst)
max_value = find_max(lst)
min_value = find_min(lst)

print("Danh sách sau khi sắp xếp:", sorted_list)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)
max_positions = [i for i, val in enumerate(lst) if val == max_value]
min_positions = [i for i, val in enumerate(lst) if val == min_value]

print("Vị trí phần tử lớn nhất:", max_positions)
print("Vị trí phần tử nhỏ nhất:", min_positions)

