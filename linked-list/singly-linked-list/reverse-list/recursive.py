# Linked list in python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    __head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node

    def __reverse(self, pointer):
        if not pointer.next:
            self.__head = pointer
            return
        
        self.__reverse(pointer.next)

        temp = pointer.next
        temp.next = pointer
        pointer.next = None

    def reverse_list(self):
        self.__reverse(self.__head)

    def display(self):
        temp = self.__head
        while temp is not None: # while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


my_list = Linked_list()

my_list.insert_at_first(3) # 3
my_list.insert_at_first(2) # 2 3
my_list.insert_at_first(1) # 1 2 3

print("Original list:")
my_list.display() # 1 2 3

my_list.reverse_list() # 3 2 1

print("Reversed list:")
my_list.display() # 3 2 1