class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedListPop:
    
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node( value )
        
        if not self.head:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    
    def pop(self):
        if not self.head:
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        return 1
    
    def print_list(self):
        
        if not self.head:
            print("Empty list: Add elements")
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next
                
            
            
            
node = LinkedListPop()
node.append(90)
node.append(78)
node.append(80)
node.pop()
node.print_list()
        