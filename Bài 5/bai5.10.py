print("Ngo Manh Nguyen MSSV: 235752021610058")
def bubble_sort(list):
  """Sắp xếp một danh sách bằng thuật toán nổi bọt.

  Args:
    list: Danh sách các phần tử cần sắp xếp.

  Returns:
    Danh sách đã được sắp xếp.
  """

  n = len(list)
  # Vòng lặp bên ngoài điều khiển số lần so sánh
  for i in range(n):
    swapped = False
    # Vòng lặp bên trong thực hiện so sánh và đổi chỗ các phần tử
    for j in range(0, n-i-1):
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
        swapped = True
    # Nếu không có lần đổi chỗ nào xảy ra, danh sách đã được sắp xếp
    if not swapped:
      break
  return list

# Nhập danh sách từ người dùng
nlist = list(map(int, input("Nhập danh sách các số (cách nhau bởi dấu cách): ").split()))

# Sắp xếp danh sách và in kết quả
sorted_list = bubble_sort(nlist)
print("Danh sách đã được sắp xếp:", sorted_list)
