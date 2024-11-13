#1)Write a python program to remove punctuations from the given string?.

import string
def remove_punctuation(input_string):
    translation_table = str.maketrans('', '', string.punctuation)
    return input_string.translate(translation_table)
input_string = input("Enter a string: ")
result = remove_punctuation(input_string)
print("String without punctuation:", result)






#2)Write a Python program to implement Heuristic search algorithm.

import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0  

    def __lt__(self, other):
        return self.h < other.h

def heuristic(a, b):
    
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first_search(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  

        
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            
            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])):
                if grid[node_position[0]][node_position[1]] != 0:  
                    continue

                if node_position in closed_set:
                    continue

                neighbor_node = Node(node_position, current_node)
                neighbor_node.h = heuristic(node_position, goal_node.position)

                
                heapq.heappush(open_list, neighbor_node)

    return None  


if __name__ == "__main__":
    
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    start = (0, 0)  
    goal = (4, 4)   

    path = greedy_best_first_search(grid, start, goal)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
