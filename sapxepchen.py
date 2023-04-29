my_list = input("Nhập vào các phần tử của list, cách nhau bởi dấu phẩy: ").split(",")
print(my_list) #Nhập vào từ bàn phím

def sap_xep(my_list):
    size = len(my_list) #Lưu độ dài của giá trị list đã nhập
    for k in range(1, size): #Vòng lặp
        temp = my_list[k] #lưu trữ giá trị của phần tử tại vị trí k trong danh sách my_list bằng biến temp
        vi_tri = k #Lưu giữ vị trí k
    # Bước lặp k: liên tục đổi chỗ phần tử thứ k với phần tử kề bên trái nó chừng nào phần tử thứ k còn nhỏ hơn phần tử đó
        while vi_tri > 0 and my_list[vi_tri-1] > temp: #Vòng lặp while với điều kiện vị trí luôn dương và giá trị phía trước (bên trái) lớn hơn temp 
            my_list[vi_tri] = my_list[vi_tri-1] #Đổi chỗ 2 vị trí 
            vi_tri -= 1 #Giảm giá trị vị trí để thực hiện bước so sánh lặp tiếp theo
    # Chèn giá trị temp (=a[k]) vào đúng vị trí
        my_list[vi_tri] = temp 
    return my_list #Trả giá trị

a = sap_xep(my_list)
print(a) #in giá trị list