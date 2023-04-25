QUEEN = "\u265B" # mã Unicode của ký tự hậu trong cờ vua
N = 8 # kích thước bảng N x N, mặc định là 8
x = 1 # biến đếm số lượng giải pháp có thể được tìm thấy

def is_safe(bang, hangngang, cot):
    # Kiểm tra xem có thể đặt quân hậu lên bảng [hangngang] [cot] hay không
    # Kiểm tra hàng ngang này trên kích thước bên trái
    for i in range(cot): # để duyệt qua các cột trước đó của bảng
        # và kiểm tra xem có quân hậu nào đang nằm trên cùng một hàng với quân hậu mà chúng ta đang xét
        # (tại hàng hangngang và cột cot)
        if bang[hangngang][i] == QUEEN: # kiểm tra xem trên hàng hangngang,
                                        # cột i của bảng đã có quân hậu (QUEEN) được đặt hay chưa
            return False # để thông báo cho chương trình rằng chúng ta không thể đặt quân hậu ở vị trí hiện tại,
                         # và chương trình sẽ thử các vị trí khác cho quân hậu đó.
    # Kiểm tra đường chéo trên bên trái
    for i, j in zip(range(hangngang, -1, -1), range(cot, -1, -1)): # kiểm tra xem quân hậu mới có an toàn
                                                                   # trên đường chéo bên trái trên của nó hay không
        if bang[i][j] == QUEEN: # kiểm tra xem ô (i, j) trên bàn cờ có chứa một quân hậu hay không
            return False
    # Kiểm tra đường chéo dưới bên trái
    for i, j in zip(range(hangngang, N, 1), range(cot, -1, -1)): # duyệt qua các ô trên đường chéo trái dưới của quân hậu mới
                                                                 # và kiểm tra tính an toàn của vị trí hiện tại
    ## range(hangngang, N, 1) là một chuỗi số nguyên liên tiếp,
    # bắt đầu từ giá trị hangngang đến giá trị N-1, với bước nhảy là 1
    # Chuỗi này tương ứng với các hàng bên dưới hàng của quân hậu mới
    ## range(cot, -1, -1) là một chuỗi số nguyên liên tiếp,
    # bắt đầu từ giá trị cot đến giá trị 0, với bước nhảy là -1
    # Chuỗi này tương ứng với các cột bên trái của vị trí của quân hậu mới
    ## Hàm zip sử dụng để lặp qua hai chuỗi này cùng lúc và trả về các cặp giá trị tương ứng từ hai chuỗi
        if bang[i][j] == QUEEN: # kiểm tra xem ô (i, j) trên bàn cờ có chứa một quân hậu hay không
            return False
    return True # nghĩa là vị trí hiện tại có thể đặt quân hậu mà không bị tấn công.

# hàm giải bài toán 8 quân hậu
def n_queen_solution(bang, cot):
    # khởi tạo biến res với giá trị FALSE,biến này sẽ được trả về cuối cùng nếu không có giải pháp nào
    res = False
    # biến toàn cục dùng để đếm số lượng giải pháp được tìm thấy.
    global x
    # Đoạn code này kiểm tra xem đã đặt quân hậu trên tất cả các cột của bàn cờ chưa nếu rồi thì in ra được 1 giải pháp
    if cot >= N:
        print(x, ": ")
        # Đoạn code này dùng để in ra bàn cờ hiện tại
        # sử dụng 2 vòng lặp for để lặp qua từng hàng và cột của bàn cờ
        # trong mỗi vòng lặp in ra giá trị của bàn cờ kết thức bằng khoảng trắng
        # sau khi in hết các ô ,chúng ta in ra một dòng trống để xuống dòng và tiếp tục in các ô trên hàng tiếp theo.
        for i in range(N):
            for j in range(N):
                print(bang[i][j], end="  ")
            print()
        print()
        # sau khi in xong bàn cờ hiện tại thì tăng giá trị của biến đếm thêm 1 đơn vị
        # rồi trả về giá trị TRUE để thông báo đã tìm thấy 1 giải pháp
        x += 1
        return True

    # code để đặt quân hậu vào bàn cờ
    # sử dụng vòng lặp for để lặp qua từng hàng trên cột,
    # với mỗi hàng thì kiểm tra quân hậu có thể đặt vào vị trí đó hay không bằng cách sử dụng hàm is_safe
    # với tham số i là số hàng cot là số cột
    for i in range(N):
        if is_safe(bang, i, cot):
            # dòng lệnh này dùng để đặt quân hậu vào vị trí (i,cot) trên bàn cờ
            # bằng cách gán giá trị "queen" cho phần tử tại vị trí đó trong bang
            bang[i][cot] = QUEEN
            # gọi hàm n_queen_solution với tham số bang và cột cot+1
            # nếu hàm trả về là True thì biến res sẽ được cập nhật thành True rồi in kết quả ra màn hình
            # nếu hàm trả về là FALSE thì gán giá trị ô(i,cot) trở lại thành "_" để thử các giá trị khác cho biến i trên cột hiện tại
            res = n_queen_solution(bang, cot + 1) or res
            bang[i][cot] = '_'
            # cuối cùng trả về giá trị biến res để biểu thị cho việc tìm được giải pháp nếu là True và không tìm thấy giải pháp nếu là False
    return res

def n_queen():
    # câu lệnh dùng để khởi tạo bàn cờ có kích thước NxN, với tất cả các ô đều chưa đặt quân hậu và được đánh dấu bằng dấu "_"
    bang = [['_' for _ in range(N)] for _ in range(N)]
    # hàm n_queen_solution(bang, 0) với tham số đầu tiên là bàn cờ mới tạo ở trên,
    # và tham số thứ hai là 0, đại diện cột đầu tiên mà quân hậu được đặt trên bàn cờ.
    y = n_queen_solution(bang, 0)
    # nếu n_queen_solution(bang,0) không trả về giải pháp nào thì in ra không tìm thấy giải pháp
    if not y:
        print("Không tìm thấy giải pháp")

if __name__ == '__main__':
    n_queen()
 