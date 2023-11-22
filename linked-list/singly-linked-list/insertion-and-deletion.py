# Linked list in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    __head = None
    __tail = None
    __count = 0

    def insert_at_first(self, data):
        new_node = Node(data)
        
        if not self.__count: # if count is zero
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node

        self.__count += 1

    def insert_at_last(self, data):
        new_node = Node(data)

        if not self.__count: # if count is zero
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node

        self.__count += 1

    def insert_at_position(self, data, position):
        if position < 0 or position > self.__count: # invalid position check
            exit(1)

        if not position: # if 0 == position:
            self.insert_at_first(data)
            return
        
        if position == self.__count:
            self.insert_at_last(data)
            return
        
        new_node = Node(data)

        temp = self.__head

        for i in range(position - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        self.__count += 1

    def delete_from_first(self):
        if not self.__head:
            exit(2)

        temp = self.__head
        self.__head = self.__head.next

        del temp

        if 1 == self.__count:
            self.__tail = None

        self.__count -= 1

    def delete_from_last(self):
        if not self.__head:
            exit(3)

        if 1 == self.__count:
            del self.__head

            self.__head = None
            self.__tail = None
        else:
            temp = self.__head

            while temp.next is not self.__tail:
                temp = temp.next

            temp.next = None

            del self.__tail

            self.__tail = temp

        self.__count -= 1

    def delete_from_position(self, position):
        if not self.__head: # if list is empty
            exit(4)

        if position < 0 or position > self.__count - 1: # invalid position check
            exit(5)

        if not position: # if 0 == position:
            self.delete_from_first()
            return
        
        if self.__count - 1 == position:
            self.delete_from_last()
            return
        
        temp_1 = self.__head

        for i in range(position - 1):
            temp_1 = temp_1.next

        temp_2 = temp_1.next
        temp_1.next = temp_2.next

        del temp_2

        self.__count -= 1

    def display(self):
        temp = self.__head
        while temp is not None: # while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


my_list = Linked_list()

my_list.insert_at_first(5) # 5
my_list.insert_at_first(4) # 4 5
my_list.insert_at_first(3) # 3 4 5
my_list.insert_at_first(2) # 2 3 4 5
my_list.insert_at_first(1) # 1 2 3 4 5

my_list.display() # 1 2 3 4 5

my_list.delete_from_first() # 2 3 4 5
my_list.display() # 2 3 4 5

my_list.delete_from_last() # 2 3 4
my_list.display() # 2 3 4

my_list.delete_from_position(1) # 2 4
my_list.display() # 2 4

my_list.delete_from_position(0) # 4
my_list.display() # 4
