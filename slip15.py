#1)Write a python Program to print Fibonacci series

def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
num_terms = int(input("Enter the number of terms: "))
fib_series = fibonacci_iterative(num_terms)
print("Fibonacci series (iterative):", fib_series)





'''2)Write a program to implement Iterative Deepening DFS algorithm.
[ Goal Node =G]'''

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def depth_limited_dfs(self, node, goal_node, depth, visited):
        if depth == 0:
            return node == goal_node
        visited.add(node)
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited and self.depth_limited_dfs(neighbor, goal_node, depth - 1, visited):
                return True
        visited.remove(node)
        return False

    def iterative_deepening_dfs(self, start_node, goal_node, max_depth):
        for depth in range(max_depth + 1):
            print(f"Searching at depth: {depth}")
            if self.depth_limited_dfs(start_node, goal_node, depth, set()):
                print(f"Reached goal node: {goal_node}")
                return True
        print(f"Goal node {goal_node} not reached within depth {max_depth}.")
        return False

if __name__ == "__main__":
    g = Graph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'), ('D', 'H'), ('D', 'I'), ('F', 'K'), (7, 8)]
    for u, v in edges:
        g.add_edge(u, v)
        
        start_node = 'A'
        goal_node = 'G'

    g.iterative_deepening_dfs(start_node, goal_node, 5)
