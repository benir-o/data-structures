class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Initial commit
class Linkedlist:
    def __init__(self):
        self.head=None
    def append_node(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node
    def print_nodes(self):
        while self.head.next is not None:
            print(self.head.data,'-->',end=" ")
            self.head=self.head.next
        print(self.head.data)


node_blocks=Linkedlist()
node_blocks.append_node(10)
node_blocks.append_node(20)
node_blocks.append_node(30)
node_blocks.append_node(40)
node_blocks.print_nodes()



