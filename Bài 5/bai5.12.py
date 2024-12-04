print("Ngo Manh Nguyen MSSV: 235752021610058")
import numpy as np

# Dữ liệu đầu vào
ma_so = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
chieu_cao = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sử dụng lexsort() để sắp xếp theo chiều cao tăng dần
sorted_indices = np.lexsort((ma_so, chieu_cao))

# In các chỉ số mô tả thứ tự sắp xếp
print("Indices of sorted data:")
print(sorted_indices)

# In dữ liệu đã được sắp xếp theo thứ tự chiều cao
print("Sorted data by height and then by student ID:")
for idx in sorted_indices:
    print(f"ma_so: {ma_so[idx]},chieu_cao:{chieu_cao[idx]}")
