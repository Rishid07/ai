
'''1)Python program that demonstrates the hill climbing algorithm to find the maximum of a
mathematical function.(For example f(x) = -x^2 + 4x)'''


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

 





#2)Write a Python program to implement Depth First Search algorithm. Refer the following graph
#as an Input for the program.[Initial node=1,Goal node=8]

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def dfs(self, start_node, goal_node):
        visited = {start_node} 
        stack = [start_node]  

        while stack:
            node = stack.pop()  

            print(node, end=' ') 

            if node == goal_node:
                print(f"\nReached goal node: {goal_node}")
                return True

            for neighbor in reversed(self.graph.get(node, [])): 
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        print(f"\nGoal node {goal_node} not reached.")
        return False

if __name__ == "__main__":
    g = Graph()
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 8), (7, 8)]
    for u, v in edges:
        g.add_edge(u, v)

    start_node = 1
    goal_node = 8
    print(f"Depth-First Search starting from node {start_node} to find node {goal_node}:")
    g.dfs(start_node, goal_node)