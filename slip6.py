#1)Write a python program to print lowercase and uppercase alphabets of string.

def print_alphabets(string):
    lowercase = []
    uppercase = []

    for char in string:
        if char.islower():
            lowercase.append(char)
        elif char.isupper():
            uppercase.append(char)
            
    print("Lowercase alphabets:", ''.join(lowercase))
    print("Uppercase alphabets:", ''.join(uppercase))

input_string = input("Enter a string: ")
print_alphabets(input_string)





##2)Write a Python program to implement Breadth First Search algorithm. Refer the following
##graph as an Input for the program.[Initial node=1,Goal node=8]'''


from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def bfs(self, start_node, goal_node):
        visited = {start_node}
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            print(node, end=' ')

            if node == goal_node:
                print(f"\nReached goal node: {goal_node}")
                return True

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print(f"\nGoal node {goal_node} not reached.")
        return False


if __name__ == "__main__":
    g = Graph()
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 8), (7, 8)]
    for u, v in edges:
        g.add_edge(u, v)

    start_node = 1
    goal_node = 8
    print(f"Breadth-First Search starting from node {start_node} to find node {goal_node}:")
    g.bfs(start_node, goal_node)