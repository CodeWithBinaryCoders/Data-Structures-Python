class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    __tail = None
    __count = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if not self.__tail:
            self.__tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.__tail.next
            self.__tail.next = new_node

        self.__count += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.__tail:
            self.__tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.__tail.next
            self.__tail.next = new_node
            self.__tail = new_node

        self.__count += 1

    def insert(self, data, position):
        if position < 0 or position > self.__count:
            exit(1)
        
        if not position:
            self.insert_at_beginning(data)
            return
        
        if position is self.__count:
            self.insert_at_end(data)
            return
        
        temp = self.__tail
        i = 0

        while i < position:
            temp = temp.next
            i += 1

        new_node = Node(data)

        new_node.next = temp.next
        temp.next = new_node

        self.__count += 1

    def display(self):
        if not self.__tail:
            print("No data")
            return
        
        temp = self.__tail.next

        print(temp.data, end=" ")
        temp = temp.next

        while temp is not self.__tail.next:
            print(temp.data, end=" ")
            temp = temp.next

        print()

my_list = Linked_list()

my_list.insert_at_beginning(2)
my_list.insert_at_beginning(1)

my_list.insert_at_end(3)
my_list.insert_at_end(4)

my_list.insert(10 ,0)
my_list.insert(20 ,5)
my_list.insert(30 ,3)

my_list.display()