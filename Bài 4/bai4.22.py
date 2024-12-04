print("Ngo Manh Nguyen MSSV:235752021610058")
def is_all_even_digits(num):
  """Kiểm tra xem tất cả các chữ số của một số có phải là số chẵn hay không"""
  while num > 0:
    digit = num % 10
    if digit % 2 != 0:
      return False
    num //= 10
  return True

def find_even_digit_numbers(start, end):
  """Tìm tất cả các số có toàn chữ số chẵn trong một khoảng cho trước"""
  result = []
  for num in range(start, end + 1):
    if is_all_even_digits(num):
      result.append(str(num))
  return ', '.join(result)

# Gọi hàm để tìm và in kết quả
result = find_even_digit_numbers(1000, 3000)
print(result)
