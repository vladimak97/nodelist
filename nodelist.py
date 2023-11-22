# Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting and deleting nodes.

# Solution:

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next_node
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next_node
            return

        current = self.head
        while current.next_node:
            if current.next_node.data == data:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

if __name__ == "__main__":
    
    linked_list = LinkedList()
    
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    
    print("linked list:")
    linked_list.display()
    
    linked_list.delete(2)
    
    print("linked list after deletion:")
    linked_list.display()
