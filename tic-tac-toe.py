def pboard(board):
    print(board["top-l"]+"|"+board['top-m']+"|"+board['top-r'])
    print("-+-+-")
    print(board["mid-l"]+"|"+board['mid-m']+"|"+board['mid-r'])
    print("-+-+-")
    print(board["low-l"]+"|"+board['low-m']+"|"+board['low-r'])

board={"top-l":" ","top-m":" ","top-r":" ","mid-l":" ","mid-m":" ","mid-r":" ","low-l":" ","low-m":" ","low-r":" "}
pboard(board)
choice=input("Enter x or o")


for i in range(9):
    position=input("enter position")
    board[position]=choice
    if choice=="x":
        choice=="o"
    elif choice=="o":
        choice=="x"
    else:
        print("Invalid choice, Pkease enter valid choice, x or o")
pboard(board)
print("Now {choice} turn")

