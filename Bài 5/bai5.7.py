print("Ngo Manh Nguyen MSSV:235752021610058")
import numpy as np

# Định nghĩa kiểu dữ liệu cho mảng có cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Tạo danh sách chi tiết sinh viên
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Tạo mảng có cấu trúc từ danh sách sinh viên
students = np.array(students_details, dtype=data_type)

# In mảng ban đầu
print("Original array:")
print(students)

# Sắp xếp mảng theo chiều cao
print("Sort by height:")
print(np.sort(students, order='height'))
