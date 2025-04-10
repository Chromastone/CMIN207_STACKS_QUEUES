from node import Node

class Stack():
    def __init__(self):
        self.top = None
    
    def __str__(self):
        pass

    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.top == None:
            print("No closed Tickets")
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data
     