#1)Write a python program to generate Calendar for the given month and year?.
#import calendar

import calendar
def display_calendar(year, month):
    print(calendar.month(year, month))
if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    display_calendar(year, month)




#2)Write a Python program to implement Depth First Search algorithm. Refer the following graph
#as an Input for the program.[Initial node=1,Goal node=7]. 


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
    
