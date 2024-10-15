class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack_Pop:
    
    def __init__(self):
        self.height = 0
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return "Empty"
        temp = self.top
        self.top = temp.next
        temp.next = None
        return "Removed"
    
    def print_stack(self):
        if not self.top:
            print("Stack is empty , please add some values")
        else:
            current = self.top
            while current:
                print(current.value)
                current = current.next
                

stack = Stack_Pop()
stack.push(19)
stack.push(454)
stack.push(33)
stack.push(22)

stack.pop()

stack.print_stack()