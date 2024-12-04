print("Ngo Manh Nguyen MSSV:235752021610058")
def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

n = int(input("Nhập số n: "))
print(f"Các số nhỏ hơn {n} có tổng ước số lớn hơn chính nó:")
for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i, end=" ")
