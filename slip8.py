'''1)write a Python program to accept a string. Find and print the number of upper case alphabets
and lower case alphabets. '''

def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")

input_string = input("Enter a string: ")
count_case(input_string)






'''2)Write a Python program to simulate n-Queens problem. '''


def print_board(queens):
    size = len(queens)
    for i in range(size):
        row = ['.'] * size
        row[queens[i]] = 'Q'
        print(" ".join(row))
    print()

def is_safe(queens, row, col):
    for r in range(row):
        if queens[r] == col or abs(queens[r] - col) == abs(r - row):
            return False
    return True

def solve_n_queens(queens, row):
    if row == len(queens):
        print_board(queens)
        return

    for col in range(len(queens)):
        if is_safe(queens, row, col):
            queens[row] = col  
            solve_n_queens(queens, row + 1)  
            queens[row] = -1  

def solve_n_queens_problem(size):
    queens = [-1] * size 
    solve_n_queens(queens, 0)


solve_n_queens_problem(4)