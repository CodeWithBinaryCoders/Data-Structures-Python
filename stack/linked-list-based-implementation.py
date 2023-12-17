# Linked list based stack implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    __top = None

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.__top
        self.__top = new_node

    def pop(self):
        if self.__top is None:
            print("Stack underflow!")
        else:
            temp = self.__top
            self.__top = self.__top.next
            del temp # explicit memory deallocation during runtime
    
    def peek(self):
        if self.__top is None:
            print("Stack empty!")
        else:
            print(self.__top.data)

# driver code
            
s = Stack()

s.push(3)
s.push(2)
s.push(1)

s.pop()

s.peek()