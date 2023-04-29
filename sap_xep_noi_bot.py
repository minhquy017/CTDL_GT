# Hàm khai báo sắp xếp nổi bọt với 2 tham số đầu vào là mảng a và kích thước của mảng n
def bubbleSort(a, n):
    # biến sorted được gán bằng giá trị False để kiểm tra xem mảng đã sắp xếp xong hay chưa
    sorted = False
    # vòng lặp for lặp qua các phần tử của mảng a từ phần tử thứ 2 đến phần tử cuối cùng của mảng
    for i in range(1, n):
        # nếu mảng chưa được sắp xếp xong thì thực hiện các câu lệnh bên dưới
        if not sorted:
            # Gán giá trị True cho biến sorted để kiểm tra mảng
            sorted = True
            # vòng lặp for lồng vào vòng lặp của bubblesort để thực hiện việc so sánh và hoán đổi vị trí các phần tử trong mảng
            # bắt đầu từ phần tử đầu tiên đến n-i-1 (giảm số phép so sánh vì sau mỗi lần lặp phần tử lớn nhất đã nằm ở vị trí cuối cùng của mảng)
            for j in range(0, n-i):
                # so sánh phần tử a[j] và a[j+1] nghĩa là 1 phần tử và phần tử tiếp theo trong mảng
                # nếu giá trị a[j] lớn hơn a[j+1] thì ta thực hiện hoán đổi vị trí 2 phần tử này    
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    # trong quá trình lặp ta thực hiện ít nhất 1 lần hoán đổi(mảng chưa được sắp xếp xong) vì thế cần gán False cho sorted để đảm bảo rằng vòng lặp tiếp tục được thực hiện để kiểm tra mảng
                    sorted = False

my_list = input("Nhập vào các phần tử của list, cách nhau bởi dấu phẩy: ").split(",")
print("List ban đầu:", my_list)
bubbleSort(my_list, len(my_list))
print("List sau khi sắp xếp:", my_list)
