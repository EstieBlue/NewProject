# This file will help me create a class robot that will be used to create the robots and their properties. 

class Robot:
    # Declaring class variables
    numRobots = 0
    
    def __init__(self, start = "", end = "", path =[], personal_bad_nodes = []):
        #Ask user for starting Node
        self.start = start
        self.end = end
        self.path = path
        self.personal_bad_nodes = personal_bad_nodes
        Robot.numRobots += 1


    def __str__(self):
        return f" Start: {self.start}, End: {self.end}, Path: {self.path}"


    def checker(point):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15", "16", "17", "18", "19", "20"]
        count = 0
        #Circles through all BFS Points to check if the point is valid
        for i in range(len(alphabet)):
            for j in range(len(numbers)):
                new_node = (alphabet[i] + numbers[j])
                #print(new_node)
                if(point == new_node):
                    return True
        return False


    def ask_Nodes(self):
        #Ask for starting Node
        starting_Node = input("Enter starting node: ")

        #Checks to see if the inputted node is real
        while (not Robot.checker(starting_Node)):
            starting_Node = input("Again Enter starting node: ")
        self.start = starting_Node

        #Ask for ending Node
        ending_Node = input("Enter ending node: ")
        #Checks to see if the inputted node is real
        while (not Robot.checker(ending_Node)):
            ending_Node = input("Again Enter ending node: ")
        self.end = ending_Node



