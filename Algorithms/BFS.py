# Using the breath-first search algorithm to traverse a graph
# This implementation uses a queue to explore nodes level by level.
# The BFS algorithm starts at a given node (the "root" node) and explores all its neighbors before moving on to the neighbors' neighbors. 
# This process continues until all reachable nodes have been visited.


#Importing the necessary libraries and modules for the BFS implementation
from collections import deque

#Initialize methods that will create the nodes and edges
# v = node
def add_node(graph, v):
    if v in graph:
        print(v, "is already present in graph")
    else:
        graph[v] = []


# v1 = node 1
# v2 = node 2
def add_edge(graph, v1, v2):
    if v1 not in graph:
        print(v1, "is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

#Initiating the graph, through a column of letters and a row of numbers, to create a grid-like structure. 
