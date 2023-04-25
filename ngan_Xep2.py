class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def display(self):
        if len(self.items) == 0:
            print("Stack rỗng")
        else:
            for i in range(len(self.items) - 1, -1, -1):
                print(self.items[i])

def main():
    stack = Stack()
    while True:
        print("\n\n======================")
        print(" STACK TEST PROGRAM ")
        print("======================")
        print(" 1. Create")
        print(" 2. Push")
        print(" 3. Pop")
        print(" 4. Display")
        print(" 5. Exit")
        print("----------------------")
        ch = int(input("Nhập số để chọn chức năng tương ứng: "))

        if ch == 1:
            stack = Stack()
            print("Khởi tạo stack")

        elif ch == 2:
            m = float(input("Nhập số thực để thêm vào stack: "))
            stack.push(m)

        elif ch == 3:
            m = stack.pop()
            if m is not None:
                print(f"Giá trị của số đẩy ra khỏi stack: {m:.3f}")
            else:
                print("Stack rỗng, không thực hiện được thao tác pop")

        elif ch == 4:
            print("Danh sách các phần tử trong stack: ")
            stack.display()

        elif ch == 5:
            print("Kết thúc!")
            break

        else:
            print("Bấm sai nút số")

if __name__ == "__main__":
    main()
