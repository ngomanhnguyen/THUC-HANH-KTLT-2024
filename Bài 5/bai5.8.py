print("Ngo Manh Nguyen MSSV:235752021610058")
def Sequential_Search(dlist, item):
    for index in range(len(dlist)):
        if dlist[index] == item:
            return index
    return -1

# Chương trình chính
n = int(input("Nhập số lượng phần tử trong danh sách: "))
dlist = []

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    dlist.append(value)

item = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm Sequential_Search
position = Sequential_Search(dlist, item)

if position != -1:
    print(f"Phần tử {item} được tìm thấy tại vị trí (index): {position}")
else:
    print(f"Phần tử {item} không có trong danh sách.")
