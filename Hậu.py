

QUEEN = "\u265B"        # unicode of chess queen-symbol
N = 8
x = 1


def is_safe(board, row, col):
    """Checking if a queen can be placed on board[row][col]."""

    # Check this row on left size
    for i in range(col):
        if board[row][i] == QUEEN:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False

    # Check lower diagonal on left size
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False

    return True

# hàm giải bài toán 8 quân hậu 
def n_queen_solution(board, col):
    # khởi tạo biến res với giá trị FALSE,biến này sẽ được trả về cuối cùng nếu không có giải pháp nào
    res = False
    # biến toàn cục dùng để đếm số lượng giải pháp được tìm thấy.
    global x
#Đoạn code này kiểm tra xem đã đặt quân hậu trên tất cả các cột của bàn cờ chưa nếu rồi thì in ra được 1 giải pháp 
    if col >= N:
        print(x, ": ")
#Đoạn code này dùng để in ra bàn cờ hiện tại   
#sử dụng 2 vòng lặp for để lặp qua từng hàng và cột của bàn cờ 
#trong mỗi vòng lặp in ra giá trị của bàn cờ kết thức bằng khoảng trắng
# sau khi in hết các ô ,chúng ta in ra một dòng trống để xuống dòng và tiếp tục in các ô trên hàng tiếp theo. 
        for i in range(N):
            for j in range(N):
                print(board[i][j], end="  ")
            print()
        print()
# sau khi in xong bàn cờ hiện tại thì tăng giá trị của biến đếm thêm 1 đơn vị rồi trả về giá trị TRUE để thông báo đã tìm thấy 1 giải pháp        
        x += 1
        return True
# code để đặt quân hậu vào bàn cờ 
# sử dụng vòng lặp for để lặp qua từng hàng trên cột, với mỗi hàng thì kiểm tra quân hậu có thể đặt vào vị trí đó hay không bằng cách sử dụng hàm is_safe
# với tham số i là số hàng col là số cột 
    for i in range(N):
        if is_safe(board, i, col):
# dòng lệnh này dùng để đặt quân hậu vào vị trí (i,col) trên bàn cờ bằng cách gán giá trị "queen" cho phần tử tại vị trí đó trong board           
            board[i][col] = QUEEN
# gọi hàm n_queen_solution với tham số board và cột col+1   nếu hàm trả về là True thì biến res sẽ được cập nhật thành true rồi in kết quả ra màn hình 
# nếu hàm trả về là FALSE thì gán giá trị ô(i,col) trở lại thành "_" để thử các giá trị khác cho biến i trên cột hiện tại 
            res = n_queen_solution(board, col + 1) or res

            board[i][col] = '_'         # backtrack
# cuối cùng trả về giá trị biến res để biểu thị cho việc tìm được giải pháp nếu là True và không tìm thấy giải pháp nếu là False
    return res


def n_queen():
    # câu lệnh dùng để khởi tạo bàn cờ có kích thước NxN, với tất cả các ô đều chưa đặt quân hậu và được đánh dấu bằng dấu "_"
    board = [['_' for _ in range(N)] for _ in range(N)]
    # hàm n_queen_solution(board, 0) với tham số đầu tiên là bàn cờ mới tạo ở trên, và tham số thứ hai là 0, đại diện cho số lượng quân hậu đã đặt trên bàn cờ.
    y = n_queen_solution(board, 0)
    # nếu n_queen_solution(board,0) không trả về giải pháp nào thì in ra "no solution exist" nghĩa là không tìm thấy giải pháp
    if not y:
        print("No solution exist!")


if __name__ == '__main__':
    n_queen()