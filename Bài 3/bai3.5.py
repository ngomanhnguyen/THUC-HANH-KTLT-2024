print("Ngô Mạnh Nguyên MSSV: 235752021610058")
a = "Hello Guy!"

def say():
    global a  # Sử dụng biến toàn cục 'a'
    a = "Vinh University"  # Thay đổi giá trị của 'a' toàn cục
    print(a)  # In giá trị của 'a' bên trong hàm

say()  # Gọi hàm say() để thay đổi giá trị của 'a'
print(a)  # In giá trị của 'a' sau khi gọi hàm
