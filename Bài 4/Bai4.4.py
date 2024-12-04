print("Ngo Manh Nguyen MSVV: 235752021610058")
input_str = input("Nhập danh sách các từ")

# Tách chuỗi thành các từ
words = input_str.split()

# In các từ theo thứ tự ngược lại
for word in reversed(words):
    print(word, end=" ")
