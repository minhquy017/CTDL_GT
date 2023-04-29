my_list = input("Nhập vào các phần tử của list, cách nhau bởi dấu phẩy: ").split(",")
print(my_list) #Nhập vào từ bàn phím

def sap_xep_chon(my_list):
    n = len(my_list)    
    for i in range(n):
        # Tìm phần tử nhỏ nhất trong đoạn chưa sắp xếp
        min_idx = i
        for j in range(i+1, n):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        
        # Đổi chỗ phần tử nhỏ nhất với phần tử đầu tiên của đoạn chưa sắp xếp
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    
    return my_list

a = sap_xep_chon(my_list)
print(a) #in giá trị list