print("Ngo Manh Nguyen MSSV:235752021610058")
import datetime as dt

# Định dạng thời gian theo chuỗi
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển đổi chuỗi thành đối tượng datetime
t1 = dt.datetime.strptime('2005-10-06T14:45:52', format)

# In các thành phần ngày, tháng, phút và giây
print('Day: ' + str(t1.day))       # Ngày
print('Month: ' + str(t1.month))   # Tháng
print('Minute: ' + str(t1.minute)) # Phút
print('Second: ' + str(t1.second)) # Giây

# Lấy ngày giờ hiện tại
t2 = dt.datetime.now()

# Tính khoảng cách giữa t2 và t1
diff = t2 - t1

# In số ngày chênh lệch
print('How many days difference? ' + str(diff.days))
