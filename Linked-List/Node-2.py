class Node:
    def __init__(self,data):
        self.data=data
        self.next=None # This is a pointer to the next node

    def append(self,data):
        new_node=Node(data)

