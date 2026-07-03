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
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15", "16", "17", "18", "19", "20"]

def create_graph():
    #Declaring the graph
    graph = {}

    count = 0

    #Creating all the nodes
    # and also adding edges horizontally -----
    for i in range(len(alphabet)):
        for j in range(len(numbers)):
            new_node = (alphabet[i] + numbers[j])


            #This creates the new nodes
            add_node(graph, new_node)
            #print(new_node)


            #Creates Nodes Horizontally
            if(count % 21):
                #print(count)
                #print(old_node + " " + new_node)
                add_edge(graph, old_node, new_node)
           
            old_node = new_node
            count += 1


    #Reseting count to 0
    count = 0


    #Creating edges vertically |||
    for i in range(len(numbers)):
        for j in range(len(alphabet)):

            new_node = (alphabet[j] + numbers[i])

            if(count % 21):
                #print(old_node + " " + new_node)
                add_edge(graph, old_node, new_node)

            old_node = new_node
            count += 1


    #Next Step is adding the diagnol lines
    #This makes edges that are diagnally   /// This direction
    # 20 x 20 grid sqaures

    for i in range(20):
        for j in range(20):
            if(i % 2 == 0 and j % 2 == 0):
                countSqaures = 2
                node1 = alphabet[i+ countSqaures] + numbers[j]


                countSqaures = 1
                node2 = alphabet[i + countSqaures] + numbers[j + countSqaures]


                #Add an edge
                #print(node1, " ", node2)
                #print("-----------")
                add_edge(graph, node1, node2)


                countSqaures = 2
                node1 = alphabet[i] + numbers[j + countSqaures]


                #Add an edge
                #print(node2, " ", node1)
                #print("-----------")
                add_edge(graph, node2, node1)


    #This makes edges that are diagnally   \\\\\ This direction
    # 20 x 20 grid sqaures
    for i in range(20):
        for j in range(20):
            if(i % 2 == 0 and j % 2 == 0):
                countSqaures = 0
                node1 = alphabet[i+ countSqaures] + numbers[j]

                countSqaures = 1
                node2 = alphabet[i + countSqaures] + numbers[j + countSqaures]

                #Add an edge
                #print(node1, " ", node2)
                #print("-----------")
                add_edge(graph, node1, node2)

                countSqaures = 2
                node1 = alphabet[i + countSqaures] + numbers[j + countSqaures]

                #Add an edge
                #print(node2, " ", node1)
                #print("-----------")
                add_edge(graph, node2, node1)

    return graph
