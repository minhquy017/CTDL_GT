
n = 8

# kiểm tra nước đi có hợp lệ hay không 
def isSafe(x, y, board):
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False
  
# in ra giải pháp cho ma trận 
def printSolution(n, board):
  
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
  
# hàm tìm giải pháp cho bài toán mã đi tuần bằng kỹ thuật quay lui
def solveKT(n):
   
# khởi tạo ma trận  
    board = [[-1 for i in range(n)]for i in range(n)]
  
# khởi tạo 2 mảng lưu tọa độ của ma trận
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
  
# khởi tạo vị trí bắt đầu
    board[0][0] = 0
  
# bộ đếm bước cho con mã trong bàn cờ
    pos = 1
  
# kiểm tra xem giải pháp có tồn tại hay không
    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        printSolution(n, board)
  
# sử dụng hàm đệ quy để tìm kiếm giải pháp  
def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):

# kiểm tra xem đã đi hết các ô trên bàn cờ hay chưa 
    if(pos == n**2):
        return True
  
# duyệt qua các bước đi của con mã trên bàn cờ
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
# gọi đệ quy tìm kiếm giải pháp tiếp theo cho quân mã            
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
  
            # nếu không tìm thấy giải pháp thì trả lại vị trí ban đầu
            board[new_x][new_y] = -1
    return False

  
  

if __name__ == "__main__":
    solveKT(n)