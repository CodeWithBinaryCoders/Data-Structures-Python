class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    __head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.__head
        self.__head = new_node

    def __recursive_print(self, pointer):
        if not pointer: # if list is empty
            return
        
        print(pointer.data, end = ' ')
        
        self.__recursive_print(pointer.next)

    def forward_print(self):
        self.__recursive_print(self.__head)
        print()

        

my_list = Linked_list()

my_list.insert_at_beginning(5) # 5
my_list.insert_at_beginning(4) # 4 5
my_list.insert_at_beginning(3) # 3 4 5
my_list.insert_at_beginning(2) # 2 3 4 5
my_list.insert_at_beginning(1) # 1 2 3 4 5

my_list.forward_print() # 1 2 3 4 5