#1)Write a program to find and display perfect numbers from list.

def get_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_number(n):
    divisors = get_divisors(n)
    return sum(divisors) == n

def find_perfect_numbers_from_list(numbers):
    perfect_numbers = []
    for num in numbers:
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

if __name__ == "__main__":
    numbers_list = [6, 28, 12, 496, 35, 8128, 100]

    perfect_numbers = find_perfect_numbers_from_list(numbers_list)
    if perfect_numbers:
        print("Perfect numbers in the list:", perfect_numbers)
    else:
        print("No perfect numbers found in the list.")







'''2)Write a Python program to simulate 8-Queens problem. '''

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

def solve_8_queens():
    size = 8
    queens = [-1] * size  
    solve_n_queens(queens, 0)

solve_8_queens()
