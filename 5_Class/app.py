def Rectangular_star(row, col):
    for i in range(row):
        for j in range(col):
            print("*", end=" ")
        print()


def Right_Half_pyramid(row, col):
    for i in range(1, row + 1):
        for j in range(i):
            print("*", end=" ")
        print()

def Left_Half_Pyramid(row, col):
    for i in range(1, row + 1):
        for j in range(row - i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print()

def Full_Pyramid(row, col):
    for i in range(1, row + 1):
        for j in range(row - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print("*", end=" ")
        print()

def menu():
    while True:
        print("\n------star pattern menu-----")
        print("1. Rectangular star")
        print("2. Right Half pyramid")
        print("3. Left Half pyramid")
        print("4. Full Pyramid")
        print("5. Exit")

        choice = input("Enter your choice (1-4): ")

        # get row and col
        row = int(input("Enter number of Rows: "))
        col = None

        if choice in ["1"]:
            col = int(input("Enter number of Cols: "))

        if choice == "5":
            print("Exited the program")
            break

        match choice:
            case "1":
                Rectangular_star(row, col)
            case "2":
                Right_Half_pyramid(row, col)
            case "3":
                Left_Half_Pyramid(row, col)
            case "4":
                Full_Pyramid(row, col)


menu()
