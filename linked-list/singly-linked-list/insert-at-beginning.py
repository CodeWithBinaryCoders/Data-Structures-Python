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

    def display(self):
        temp = self.__head
        while temp is not None: # while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


my_list = Linked_list()

my_list.insert_at_first(1) # 1
my_list.insert_at_first(2) # 2 1
my_list.insert_at_first(3) # 3 2 1

my_list.display()