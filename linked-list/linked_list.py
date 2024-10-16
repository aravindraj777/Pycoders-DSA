class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_linked_list(self):
        if not self.head:
            return "Empty"
        current = self.head
        while current:
            print(current.data)
            current = current.next


node = LinkedList()
node.append(10)
node.append(20)
node.append(30)

node.print_linked_list()
