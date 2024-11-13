#1)Write a python program to accept a number and check whether prime or not. 

def is_prime(num):
    
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            return False
    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")





'''2)Write a Python program to simulate 4-Queens problem.'''


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

def solve_4_queens():
    size = 4
    queens = [-1] * size  
    solve_n_queens(queens, 0)

solve_4_queens()