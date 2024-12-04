import numpy as np

# Định nghĩa kiểu dữ liệu cho mảng có cấu trúc
data_type = [('Ten ', 'S15'), ('Lop', int), ('Chieu cao', float)]

# Tạo danh sách chi tiết sinh viên
students_details = [
    ('Nguyen', 5, 48.5),
    ('Huy', 6, 52.5),
    ('An', 5, 42.1),
    ('quyen', 5, 40.11)
]

# Tạo mảng có cấu trúc từ danh sách sinh viên
students = np.array(students_details, dtype=data_type)

# In mảng ban đầu
print("Original array:")
print(students)

# Sắp xếp mảng theo lớp, sau đó theo chiều cao nếu lớp bằng nhau
sorted_students = np.sort(students, order=['Lop', 'Chieu cao'])

# In kết quả sau khi sắp xếp
print("Sorted array:")
print(sorted_students)
