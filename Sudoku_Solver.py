test_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],   
    [6, 0, 0, 0, 7, 5, 0, 0, 9],   
    [0, 0, 0, 6, 0, 1, 0, 7, 8],   
    [0, 0, 7, 0, 4, 0, 2, 6, 0],   
    [0, 0, 1, 0, 5, 0, 9, 3, 0],   
    [9, 0, 4, 0, 6, 0, 0, 0, 5],   
    [0, 7, 0, 3, 0, 0, 0, 1, 2],   
    [1, 2, 0, 0, 0, 7, 4, 0, 0],   
    [0, 4, 9, 2, 0, 6, 0, 0, 7]   
]


"""The main function that helps solve the puzzle recursively with help from the helper functions"""
def solve_sudoku(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


"""Function to check the validity of the numbers placed on the board"""
def valid(board, num, pos):

    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # checking column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    # checking box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 +3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True


"""Function to help print the board in a user friendly way"""
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


"""Function to help find the empty slots on the board"""
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row, column
    return None


"""Printing out the outputs of a solved board"""
print_board(test_board)
solve_sudoku(test_board)
print("_____________________________")
print("")
print("*********The solved Sudoku**************")
print("_____________________________")
print("")
print_board(test_board)