def part(m, n):
    if m == 0:
        return 1
    elif n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    elif m < n:
        return part(m, m)
    else:
        return part(m, n-1) + part(m-n, n)

def chia_thuong():
    print("BAI TOAN CHIA THUONG")
    m = int(input("Nhap m (phan thuong): "))
    n = int(input("Nhap n (so sinh vien): "))
    print(f"{m} phan thuong, {n} sinh vien se co {part(m,n)} cach chia")

chia_thuong()
              