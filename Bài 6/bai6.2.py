print("Ngo Manh Nguyen MSSV: 235752021610058")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        """
        Khởi tạo đối tượng Hinhchunhat với chiều dài và chiều rộng.
        """
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        """
        Tính và trả về diện tích hình chữ nhật.
        """
        return self.chieu_dai * self.chieu_rong


hinh = Hinhchunhat(5, 6)  # Hình chữ nhật có chiều dài 6, chiều rộng 5
dien_tich = hinh.tinh_dien_tich()
print(f"Diện tích hình chữ nhật là: {dien_tich}")
