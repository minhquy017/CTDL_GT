import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Định nghĩa màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Định nghĩa kích thước bàn cờ và kích thước ô cờ
SIZE = 64
WIDTH = HEIGHT = SIZE * 8

# Tạo cửa sổ trò chơi
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Đặt tiêu đề cho cửa sổ trò chơi
pygame.display.set_caption("8 Quân Hậu")

# Hàm vẽ bàn cờ
def draw_board():
    for row in range(8):
        for col in range(8):
            x = col * SIZE
            y = row * SIZE
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x, y, SIZE, SIZE))

# Hàm vẽ quân hậu
def draw_queen(x, y):
    crown = pygame.image.load("crown.png") # Thay đổi đường dẫn tùy vào nơi lưu trữ hình ảnh crown.png
    crown = pygame.transform.scale(crown, (SIZE, SIZE))
    screen.blit(crown, (x, y))

# Hàm hiển thị lời giải
def show_solution(solution):
    for row in range(8):
        col = solution[row]
        draw_queen(col * SIZE, row * SIZE)

# Hàm chính để thực thi chương trình
def main():
    # Vòng lặp chính
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Vẽ bàn cờ
        draw_board()

        # Giải bài toán 8 quân hậu và hiển thị lời giải
        solution = [0, 4, 7, 5, 2, 6, 1, 3] # Thay đổi giá trị của solution tùy vào bài toán được giải
        show_solution(solution)

        # Hiển thị cửa sổ trò chơi
        pygame.display.flip()

# Kiểm tra nếu chương trình được thực thi trực tiếp
if __name__ == "__main__":
    main()
