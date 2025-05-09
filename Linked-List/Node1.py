# Node class represents each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the data
        self.next = None      # Pointer to the next node

# LinkedList class manages the linked list
class LinkedList:
    def __init__(self):
        self.head = None      # Start with an empty list

    # Append a node to the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node
        
        if not self.head:      # If the list is empty
            self.head = new_node
            return
        
        # Otherwise, traverse to the end and add the new node
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    # Print the entire list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a LinkedList and perform operations
if __name__ == "__main__":
    ll = LinkedList()         # Create a new linked list

    # Append nodes
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # Print the list
    print("Linked List:")
    ll.print_list()
