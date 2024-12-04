print("Ngo Manh Nguyen MSSSV:235752021610058")
def tam_giac_pascal(n):
    tam_giac = []
    for i in range(n):
        hang = [1] * (i + 1)
        for j in range(1, i):
            hang[j] = tam_giac[i - 1][j - 1] + tam_giac[i - 1][j]
        tam_giac.append(hang)
    
    for hang in tam_giac: 

        print(*hang)

n = int(input("Nhập số dòng: "))
tam_giac_pascal(n)
