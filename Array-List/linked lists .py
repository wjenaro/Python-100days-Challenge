class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ' if current.next else '')
            current = current.next
        print("=>  End")
# Create a new LinkedList
linked_list = LinkedList()

# Append elements to the list
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Display the linked list
linked_list.display()  # Output: 10 -> 20 -> 30
