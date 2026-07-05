# This file will help me create a class robot that will be used to create the robots and their properties. 

class Robot:
    def __init__(self, name, start, end, path =[]):
        self.name = name
        self.start = start
        self.end = end
        self.path = path

    def __str__(self):
        return f"Robot: {self.name}, Start: {self.start}, End: {self.end}, Path: {self.path}"



