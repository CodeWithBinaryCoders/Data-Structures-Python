class Stack:
    def __init__(self):
        self.__arr = []

    def __check_empty(self): # private
        if not len(self.__arr):
            return True
        return False
    
    def push(self, data):
        self.__arr.append(data)

    def pop(self):
        if self.__check_empty():
            print("Stack underflow!")
        else:
            self.__arr.pop()

    def peek(self):
        if self.__check_empty():
            print("Stack empty!")
        else:
            print(self.__arr[len(self.__arr) - 1])

    def is_empty(self):
        if self.__check_empty():
            print('1')
        else:
            print('0')

    def clear_stack(self):
        self.__arr.clear()

# driver code

s = Stack()

s.push(1)
s.push(2)
s.push(3)

s.pop()

s.peek()

s.is_empty()

s.clear_stack()

s.is_empty()