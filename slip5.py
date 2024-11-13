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