print("Ngo Manh Nguyen MSSV: 235752021610058")
chuoi = input("Nhập chuỗi: ")
chuoi_moi = ""
for ky_tu in chuoi:
    if not ky_tu.isdigit():
        chuoi_moi += ky_tu
print("Chuỗi mới:", chuoi_moi)
