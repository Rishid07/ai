'''1) Write a python program to sort the sentence in alphabetical order?'''


import string
def sort_sentence(sentence):
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator)
    words = sentence.split()
    words.sort(key=str.lower)
    sorted_sentence = ' '.join(words)
    return sorted_sentence
input_sentence = input("Enter a sentence: ")
sorted_sentence = sort_sentence(input_sentence)
print("Sorted sentence:", sorted_sentence)






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


solve_n_queens_problem(6)