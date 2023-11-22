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
        
        if position == self.__count:
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

    def delete_from_beginning(self):
        if not self.__tail: # if self.__tail is None:
            exit(2)

        if self.__tail.next is self.__tail: # only single node is present
            del self.__tail

            self.__tail = None
        else:
            temp = self.__tail.next
            self.__tail.next = temp.next

            del temp

        self.__count -= 1

    def delete_from_end(self):
        if not self.__tail: # if self.__tail is None:
            exit(3)

        if self.__tail.next is self.__tail: # only single node is present
            del self.__tail

            self.__tail = None
        else:
            temp = self.__tail

            while self.__tail.next is not temp:
                self.__tail = self.__tail.next
            
            self.__tail.next = temp.next

            del temp

        self.__count -= 1

    def delete_from_position(self, position):
        if not self.__tail: # if list is empty
            exit(4)

        if position < 0 or position > self.__count - 1: # invalid position
            exit(5)

        if position == 0:
            self.delete_from_beginning()
            return
        
        if position == self.__count - 1:
            self.delete_from_end()
            return
        
        temp = self.__tail.next

        for i in range(position - 1):
            temp = temp.next

        remove = temp.next
        temp.next = remove.next

        del remove

        self.__count -= 1

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

my_list.insert_at_end(1) # 1
my_list.insert_at_end(2) # 1 2
my_list.insert_at_end(3) # 1 2 3
my_list.insert_at_end(4) # 1 2 3 4
my_list.insert_at_end(5) # 1 2 3 4 5
my_list.insert_at_end(6) # 1 2 3 4 5 6
my_list.insert_at_end(7) # 1 2 3 4 5 6 7

print("Before deletion:")
my_list.display() # 1 2 3 4 5 6 7

my_list.delete_from_beginning() # 2 3 4 5 6 7
my_list.delete_from_end() # 2 3 4 5 6
my_list.delete_from_position(2) # 2 3 5 6
my_list.delete_from_beginning() # 3 5 6
my_list.delete_from_end() # 3 5

print("After deletion:")
my_list.display() # 3 5