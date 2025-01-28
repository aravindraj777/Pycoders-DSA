class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top  = new_node
        self.height += 1
        return True

    def print_stack(self):
        if not self.top:
            print("Stack is empty")
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

stack = Stack()
stack.push(20)
stack.push(56)
stack.push(22)
stack.push(12)

stack.print_stack()