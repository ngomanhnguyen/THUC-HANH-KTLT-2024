print("Ngo Manh Nguyen MSSV:235752021610058")
def sieve_of_eratosthenes(limit):
    """
    Trả về danh sách các số nguyên tố nhỏ hơn 'limit' bằng Sàng Eratosthenes.
    """
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    return [num for num, prime in enumerate(is_prime) if prime]

# Giới hạn 1 triệu
limit = 1000000
prime_numbers = sieve_of_eratosthenes(limit)

# Tạo tuple P gồm các số nguyên tố nhỏ hơn 1 triệu
P = tuple(prime_numbers)

# In ra một phần của tuple để kiểm tra
print(P[:10])  # In 10 số nguyên tố đầu tiên để kiểm tra
print(f"Số lượng số nguyên tố nhỏ hơn 1 triệu: {len(P)}")
