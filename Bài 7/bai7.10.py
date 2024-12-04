print("Ngo Manh Nguyen MSSV: 235752021610058")
def tim_tu_dai_nhat(van_ban):
  """Tìm những từ dài nhất trong một văn bản.

  Args:
    van_ban: Đoạn văn bản cần tìm kiếm.

  Returns:
    Một danh sách chứa các từ dài nhất.
  """

  # Chia văn bản thành các từ, loại bỏ các ký tự đặc biệt
  tu_list = van_ban.split()
  tu_list = [tu.strip(",.!?;:") for tu in tu_list]

  # Tìm độ dài lớn nhất của các từ
  do_dai_lon_nhat = max(len(tu) for tu in tu_list)

  # Tìm các từ có độ dài bằng độ dài lớn nhất
  tu_dai_nhat = [tu for tu in tu_list if len(tu) == do_dai_lon_nhat]

  return tu_dai_nhat

# Ví dụ sử dụng:
van_ban = "Đây là một đoạn văn bản mẫu để chúng ta thử nghiệm chương trình tìm từ dài nhất."
ket_qua = tim_tu_dai_nhat(van_ban)
print("Các từ dài nhất là:", ket_qua)
