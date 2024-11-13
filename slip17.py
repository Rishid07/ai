'''1)Python program that demonstrates the hill climbing algorithm to find the maximum of a
mathematical function.'''


import random

def objective_function(x):
    return -x**2 + 4*x

def hill_climbing(starting_point, step_size, max_iterations):
    current_solution = starting_point
    current_value = objective_function(current_solution)

    for iteration in range(max_iterations):
        neighbors = [current_solution - step_size, current_solution + step_size]

        neighbor_values = [objective_function(neighbor) for neighbor in neighbors]

        best_neighbor_value = max(neighbor_values)
        best_neighbor_index = neighbor_values.index(best_neighbor_value)
        best_neighbor = neighbors[best_neighbor_index]

        if best_neighbor_value > current_value:
            current_solution = best_neighbor
            current_value = best_neighbor_value
        else:
            
            break

    return current_solution, current_value


if __name__ == "__main__":

    starting_point = random.uniform(-10, 10) 
    step_size = 0.1  
    max_iterations = 100 


    max_point, max_value = hill_climbing(starting_point, step_size, max_iterations)

    print(f"Starting point: {starting_point}")
    print(f"Maximum found at x = {max_point}, f(x) = {max_value}")

 





'''2)Write a Python program to implement A* algorithm. Refer the following graph as an Input for
the program.[ Start vertex is A and Goal Vertex is G] '''

import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name  
        self.parent = parent  
        self.g = g  
        self.h = h  
        self.f = g + h 
    
    def __lt__(self, other):
        
        return self.f < other.f

def a_star(graph, start, goal, heuristic):
    open_list = []  
    closed_list = set()  

    
    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)  

        
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  

        closed_list.add(current_node.name)

        
        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue  
            
            g_cost = current_node.g + cost
            h_cost = heuristic[neighbor]
            neighbor_node = Node(neighbor, current_node, g_cost, h_cost)
            
            
            if not any(node.name == neighbor and node.f <= neighbor_node.f for node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3, 'G': 1},
    'G': {'E': 1}
}


heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0,
    'G': 0
}


start = 'A'
goal = 'G'
path = a_star(graph, start, goal, heuristic)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")

