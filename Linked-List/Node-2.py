class Node:
    def __init__(self,data):
        self.data=data
        self.next=None # This is a pointer to the next node

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        current_node=Node(data)
