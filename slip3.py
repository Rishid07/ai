#1)Write a python program to remove punctuations from the given string?.

import string
def remove_punctuation(input_string):
    translation_table = str.maketrans('', '', string.punctuation)
    return input_string.translate(translation_table)
input_string = input("Enter a string: ")
result = remove_punctuation(input_string)
print("String without punctuation:", result)





#2)Write a Python program to implement Depth First Search algorithm. Refer the following graph
#as an Input for the program.[Initial node=2,Goal node=7].


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
 
