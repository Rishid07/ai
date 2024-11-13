#1)Write a python program to implement List operations(any 5 operations) 

my_list = [10, 20, 30, 40, 50]
my_list.append(60)
print("After Append:", my_list)

my_list.insert(2, 25)  
print("After Insert:", my_list)

my_list.remove(30) 
print("After Remove:", my_list)

popped_element = my_list.pop(3) 
print("After Pop:", my_list)
print("Popped Element:", popped_element)

my_list.reverse()
print("After Reverse:", my_list)

my_list.sort()
print("After Sort:", my_list)

my_list.extend([70, 80, 90])
print("After Extend:", my_list)

count_20 = my_list.count(20)  
print("Count of 20:", count_20)






#2)Write a Python program to implement heuristic search algorithm 

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

