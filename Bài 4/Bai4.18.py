print("Ngo Manh Nguyen MSSV:235752021610058")
def fibonacci_list(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

n = int(input("Nhập số nguyên n: "))
fib_numbers = fibonacci_list(n)
print(f"Các số Fibonacci nhỏ hơn {n}: {fib_numbers}")
