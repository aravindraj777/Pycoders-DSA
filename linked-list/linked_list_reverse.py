class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListReverse:
    
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def print_linked_list(self):
        if not self.head:
            return 'Empty linkedList'
        current = self.head
        while current:
            print(current.value)
            current = current.next

linked_list = LinkedListReverse()
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
linked_list.append(60)

linked_list.print_linked_list()