print("Ngo Manh Nguyen MSSV:235752021610058")
def tim_tu_dai_nhat(chuoi):
  """Tìm từ dài nhất trong một chuỗi

  Args:
    chuoi: Chuỗi cần tìm từ dài nhất

  Returns:
    Một list chứa các từ dài nhất
  """

  # Tách chuỗi thành list các từ
  cac_tu = chuoi.split()

  # Tìm độ dài lớn nhất của các từ
  do_dai_lon_nhat = len(max(cac_tu, key=len))

  # Lọc ra các từ có độ dài bằng độ dài lớn nhất
  tu_dai_nhat = [tu for tu in cac_tu if len(tu) == do_dai_lon_nhat]

  return tu_dai_nhat

# Nhập chuỗi từ bàn phím
chuoi_nhap = input("Nhập dãy từ: ")

# Gọi hàm tìm từ dài nhất và in kết quả
ket_qua = tim_tu_dai_nhat(chuoi_nhap)
print("Các từ dài nhất là:", ket_qua)
