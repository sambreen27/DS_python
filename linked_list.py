#Linked list is a data structure consisting of a collection of nodes which together represent a sequence.
#Linked lists are not stored in contiguous memory locations; they are instead chained by an element storing address location of next element. This makes insertion very easy. 
#####
#Sunday, June 14, 2020

from __future__ import print_function

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None

    #inserts data beginning of linked list
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def printList(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        
        itr = self.head
        LinkedListString = ' '

        while itr:
            LinkedListString += str(itr.data) + ' --> '
            itr = itr.next

        print(LinkedListString)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next= Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    #returns lenght of our linked list 
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    #remove element at given index
    def remove_element(self, index):
        if index < 0 or index >= self.get_lenght():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

        #insert element at given index
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_lenght():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    print("\n")
    ll.insert_values(["22", "33", "44", "55"])
    print( "\n", "Lenght of initial linked list: ", ll.get_lenght())
    ll.printList()

    ll.insert_at_beginning(46)
    ll.insert_at_beginning(87)
    ll.insert_at_end(98)
    print( "\n", "Lenght of linked list after inserting elements: ", ll.get_lenght())
    ll.printList()

    ll.remove_element(2)
    ll.remove_element(3)

    print("\n", "Lenght of linked list after removing two elements: ", ll.get_lenght())
    ll.printList()

    ll.insert_at_beginning(5)
    ll.insert_at_beginning(42)
    ll.insert_at_beginning(29)
    print("\n", "Lenght of linked list after inserting elements again: ", ll.get_lenght())
    ll.printList()

    ll.insert_at(3, 100)
    ll.insert_at(5, 222)
    ll.insert_at(7, 333)
    print("\n", "Lenght of linked list after inserting elements at given index: ", ll.get_lenght())
    ll.printList()
    print("\n")
            

