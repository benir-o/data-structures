# Linked-list
Class Group Assignment.

**Name**: Kabese, Gabriel Osugo 
**Admission Number**: 192083

**Name**: Omondi, Angela Achieng
**Admission Number**: 189545

**Name**: Odeny, Benir Omenda
**Admission Number**: 192559

**Name**: Ikubu, Brian Mathara
**Admission Number**: 189736

# Code-explanaion:
**We created a class Node, then proceeded to create a constructor which we instantiated and made it point to the next node. We then created a class "Linked List" and started it off to be empty. We then created a constructor to append the node at the end of the list to contain data. We then created a new node with a loop which checked if the list was empty, at which point it would return the list otherwise, it would move to the end of the list and add a new node. We then added the if __name__ == "__main__":  to indicate that the code block below it should only be executed when the script is run directly & not when it is imported as a module in another python file. We then appended the nodes & printed the list.**

# Implementing a Linked list with Python
In this explanation article, we will use the following diagram to implement a python linked list.<br>
Take a look at the diagram below.
<br>
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fuploads%2F20220712172013%2FSinglelinkedlist.png&f=1&nofb=1&ipt=b4489608e5e97e9da45baf15d45caf3e4ce421f280309e373c9e2e0f91824357" alt="Strathmore University Logo" width="800">
## Strategy
First, we need to create a node class, followed by a linked list class. The node class will store the data and the pointers while the 
linked list class stores the nodes themselves.
It then follows that the linked list class will have nodes with data and pointers linked to other nodes, depending on the size of the linked list.

### 1. Creating a Node class 
Nodes will contain data and pointers to the next nodes.
```Python
class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None
```
To keep things simple, our node class is okay since it has the attributes that we want to focus on. However, in other implementations
we could use more attributes.
The two attributes we have added are `data` and `next`

### 2. Creating a Linked List class
First, since our linked list will be empty, we set the head node to be none since initially it won't take in any data value.
```Python
class Linkedlist:
    def __init__(self):
        self.head=None
```


The linked list class represents the whole diagram while the node class represents the nodes themselves.<br>
By observation, the first node of the `linked list` class will be called the `head` node, which at the moment has no data since
our linked list is empty.<br>
For the `linked list` class, we need to add functionality to include new nodes which will take consecutive positions, dependent on some
certain conditions.<br>
The conditions are as follows<br>

### Step by step implementation
#### 1. Creating an append function to allow addition of nodes
We create a function that takes in a node and appends it to the linked list. However for an empty linked list, if we append for the first time then the new node is our head node.<br>
The following code shows the steps taken to make the head node the new node, given that the linked list is empty.
```python
    def append_node(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
```
#### 2. Handling addition of new nodes if our linked list is not empty
If we are not appending for the first time, then it means a head node already exists. <br>
If the head node already exists, then we define a variable called `current_node` which will initially be our `head` node.<br>
```python
        else:
            current_node=self.head
```
#### 3. Looping through the nodes until we find a node with a pointer that does not point to any data value
Now we need to check if the pointer of the current node points a value that is in the next node. We do this using a while loop<br>
If the current node's pointer is not null (it is pointing to data in a consecutive node), then we would want to loop through all the nodes
until we find a node with a pointer which is **NOT** pointing to any data value.
```python
            while current_node.next is not None:
                current_node=current_node.next
```
After the while loop, we reach a node that has a pointer **NOT** pointing to any data. At this moment is when we set the value of the next node after the current node to be the `new_node` which we had created at the beginning of our function.
```python
            current_node.next=new_node
```
The whole function would look like this.
```python
    def append_node(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node
```
With the function above, one can be able to instantiate an object of the linked list class and append nodes to that specific linked list.<br>
However, we could add another function that prints the items in the nodes.

### Printing out items in our linked list class.
To print out items in our linked list class, we create a function that checks if the pointer of our head node is not null. If the condition is true, we 
print the value of the head node's data and then update the head node variable to be the value of the next node.
We repeat the process until the next node is non-existent. This means we are at the **last** node. And for such, we just print the data
of the last node since we we continuously updated our head node through the loop.
```python
    def print_nodes(self):
        while self.head.next is not None:
            print(self.head.data,'-->',end=" ")
            self.head=self.head.next
        print(self.head.data)
```

# Authors
Benir Odeny, Angela Omondi, Koi JoyJudy, Gabriel Osugo, Brian Mathara
