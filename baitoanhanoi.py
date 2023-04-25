def bai_toan_ha_noi(n,thapnguon,thapdich,thaptrunggian):
    if n ==1:
        print("chuyển đĩa 1 từ " , thapnguon ,"sang",thapdich)
    else:
        bai_toan_ha_noi(n-1,thapnguon,thaptrunggian,thapdich)
        print("chuyển đĩa ",n,"từ tháp",thapnguon,"sang",thapdich)
        bai_toan_ha_noi(n-1,thaptrunggian,thapdich,thapnguon)

n = int(input("nhập số cần tìm :"))
bai_toan_ha_noi(n,"A","C","B")        
