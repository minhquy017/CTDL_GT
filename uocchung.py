def uoc_chung_lon_nhat(a,b):
    while b!=0:
        tam= a%b
        a = b
        b = tam
    print("ước chung lớn nhất của 2 số nguyên là :",a)   

a = int(input("nhập số nguyên a :"))
b= int(input("nhập số nguyên b :"))
uoc_chung_lon_nhat(a,b)
