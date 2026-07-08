# Using the breath-first search algorithm to traverse a graph
# This implementation uses a queue to explore nodes level by level.
# The BFS algorithm starts at a given node (the "root" node) and explores all its neighbors before moving on to the neighbors' neighbors. 
# This process continues until all reachable nodes have been visited.


#Importing the necessary libraries and modules for the BFS implementation
from collections import deque
from test import Robot

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



#Finding the shortest path method
def Shortest_path(graph, bad_nodes, startNode, target):
    #Create a visited dictionary ???


    #Making sure startNode and target node are present in the graph
    if startNode not in graph:
            print(startNode, "not in graph!")
    elif target not in graph:
            print(target, "not in graph!")


    #Once confirmed that both start node and target node are within graph
    # then this
    else:
         #Visited dictionary that will store visited node and parent node
         visited = {}


         #Help figure out the shortest path between two nodes
         #This comes from the import
         queue = deque()


         # Key-value pair
         # key is the starting node, and its value is none because the starting node is the parent
         visited[startNode] = None


         queue.append(startNode)

         # Step 1: Remove node from queue
         # Step 2: Check node is target node
         # Step 3: if yes, return path
         # Step 4: if not find adjacent nodes of removed node


        # Until there is no more in queue, it will evaluate to false
         while queue:
              # To store the removed element from the queue
            current = queue.popleft()


              # Check if the removed element(node) is the target node
            if current == target:
                   # If it is target, then we need to get it to give us path
                    #Creating list to store the path
                path = []


                # Basically we are going back each time to get the parent node
                # until we are back at the starting node. This will create path from starting node
                # to target node
                # A parent node is just the node that came before the current node
                # Going  until current is equal to None, which means it is at starting point
                while current:
                    #Adding target node to the path
                    path.append(current)


                    # Adding parent node using the visited dictionary
                    current = visited[current]


                #Now we have a path but is in the reversed order
                # Therefore to reverse it
                return path[::-1]
           
            # What we do if the removed node is not the target node then
            for i in graph[current]:
                 #Then check adjacent nodes


                 # if visited then do nothing, if NOT
                 if i not in visited:
                   
                    ## Ig right here will be where we add an if statement that says if node is not on the evil node list then continue to search
                    if i not in bad_nodes:
                        # i is the adjacent node
                        # current is the parent node
                        visited[i] = current
                        queue.append(i)



def createRobots(num):
    #List of all the robots that will be created
    robot_list = [0]*num

    for i in range(num):
        #Adding to list
        new_robot = Robot()
        robot_list[i] = new_robot

        #Calls the ask_Nodes method to ask for starting and ending nodes
        # The information will be stored inside the robot class
        new_robot.ask_Nodes()

        #Take the obstacles/bad_nodes of the maze into thier personal_bad_nodes attribute
        #This  would also mean bad_nodes would have to be a parameter for createRobots method
        new_robot.personal_bad_nodes = bad_nodes

    return robot_list

# Create a compare path method that will compare the paths of the robots and see if they intersect or not
def creating_paths(num_robot, robot_list, bad_nodes):
  
    for i in range(num_robot):
        Start_node = robot_list[i].start
        End_node = robot_list[i].end

        #Store result in grid path
        result = Shortest_path(graph1, bad_nodes, Start_node, End_node)

        #Saving the path in its object (Robot Class)
        robot_list[i].path = result
        print(result)
        print("-----------")



def compare_paths(robot1, robot2):
    #Now its time to check each robot path to see if they do not intersect a node at the same time
    print("Running the Comparing Path Program")
    path1 = robot1.path
    path2 = robot2.path
    print(path1)
    print(path2)


    # Right now it only works if both of them are the same length
    # In order to solve the issue we need to get the path that is the longest
    path1_Longer = False
    size = 0
    if(len(path1) >= len(path2)):
        size = len(path1)
        path1_Longer = True
    elif(len(path1) < len(path2)):
        size = len(path2)
        path1_Longer = False


    #This will iterate through 2 paths, checking if they have the same coordinates at the same place
    for i in range(size):

        #Since the for loop goes for the larger path, then the shorter path will eventually be out of indexes to compare
        # This way the shorter path will stop when its at its end and will continue to check the last position with the longer path coordinates
        # Until there is no more of the longer path
        if(path1_Longer):
            long_path = path1[i]

            if(not i >= len(path2)):
                short_path = path2[i]
        else:
            long_path = path2[i]
            if(not i >= len(path1)):
                short_path = path1[i]


        if(long_path == short_path):
            print("Collide At Position ", (i+1))
            # I will add the previous node, that the short path was on, to the short path of were it intersects
                #Identify short path, is it path 1 or path 2
            if(path1_Longer):
                if(i <= len(path2)):
                    #Then Path2 is the shorter path AND Still going
                    path2.insert((i-1), path2[i-1])
                else:
                    #Did not take into account that the short path will run out, and there is a collision afterwards
                    path2.insert((len(path2)-1), path2[(len(path2)-1)])
            else:
                if(i <= len(path1)):
                    #Then Path1 is the shorter path AND Still going
                    path1.insert((i-1), path1[i-1])
                else:
                    #There is a collision after the short path has run out
                    path1.insert((len(path1)-1), path1[(len(path1)-1)])

    print("Finished Paths")
    print(path1)
    print(path2)

    #Saves the new paths to its robot object, for path attribute
    robot1.path = path1
    robot2.path = path2



# Did abosupltly nothing 
def double_check(robot1, robot2): 
    print("Going to solve previous issue")
    path1 = robot1.path
    path2 = robot2.path

    # Getting the longer path
    path1_Longer = False
    size = 0

    # Grabs the longest path to set it as the size
    if(len(path1) >= len(path2)):
        size = len(path1)
        path1_Longer = True
    elif(len(path1) < len(path2)):
        size = len(path2)
        path1_Longer = False

    for i in range(size):         # This line is also not full proof, could change it to a while loop

        #It would cause an error if it executed on the first try, since I use i-1
        if (i > 0):
            # Sets the next point of the paths, making sure the path has not ended
            # Could cause some potencial problems?????
            if(path1_Longer):
                new_path1 = path1[i]
                if(not i >= len(path2)):
                    new_path2 = path2[i-1]
            else:
                new_path2 = path2[i-1]
                if(not i >= len(path1)):
                    new_path1 = path1[i]

            # Checks if they are the same
            if (new_path1 == new_path2):      
                print("Bomb")
                print("First", path1[i])
                print("Second", path2[i-1])

                # The bad node is added to the robots own personal_bad_node list
                # Then create a new path based on the new bad nodes
                robot2.personal_bad_nodes.append(new_path1)
                start = robot2.start
                end = robot2.end
                
                path2 = Shortest_path(graph1, robot2.personal_bad_nodes, start, end)

            #This is an extra check that ensures, no robot will be at a node at the same time
            if(new_path1 == new_path2):
                compare_paths(robot1, robot2)

    # Saving it to the robot object
    robot1.path = path1
    robot2.path = path2


# Trying out the BFS implementation
graph1 = create_graph()

bad_nodes = ["C12", "C13", "C14", "C15", "C16", "D12", "D16", "E12", "E16", "F12", "F16", "G12", "G16", "H12", "H16", "I12", "I13", "I14", "I15", "I16"]

new_robots_list = createRobots(2)
creating_paths(2, new_robots_list, bad_nodes)
compare_paths(new_robots_list[0], new_robots_list[1])
double_check(new_robots_list[0], new_robots_list[1])
