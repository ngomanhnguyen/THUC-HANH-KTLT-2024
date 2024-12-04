print("Ngo Manh Nguyen MSSV:235752021610058")
class Nguoi:
    def getGender(self):
        return "Không xác định"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Sử dụng
nam = Nam()
nu = Nu()

print(nam.getGender())  # Output: Nam
print(nu.getGender())   # Output: Nữ
