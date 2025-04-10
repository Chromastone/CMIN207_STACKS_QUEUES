from node import Node

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
     # type: ignore
    
    def __str__(self):
        openTickets = ""
        traverser = self.front
        while traverser != None:
            openTickets += str(traverser.data) + "\n"
            traverser = traverser.next
        return openTickets
    
    def enqueue(self, data):
        temp = Node(data)
        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    def dequeue(self, data):
        if self.front == None:
            print("There are no tickets")
        else:
            temp = self.front
            self.front = temp.next
            return temp.data
        