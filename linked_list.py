import numpy as np

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("The Linked list is empty.")

        iterator = self.head
        linkedListString = ''

        while iterator:
            linkedListString += str(iterator.data) + '-->'
            iterator = iterator.next
        
        print(linkedListString)

    def insert_at_end(self, data):
        # if the linked list is empty.
        if self.head is None:
            self.head = Node(data, None)    # making the new node, head
            return

        # if not empty
        iterator = self.head
        
        while iterator.next:    # loops when it has a value
            iterator = iterator.next    # going to the last value

        # and inserting the new node at the last
        iterator.next = Node(data, None)
    
    # takes a list of values as a input and will create a new linked list
    def insert_values(self, data_list):
            
        self.head = None    # Avoiding all the current values and want to insert new values
            
        for data in data_list:
            self.insert_at_end(data)
    
    # length of the linked list
    def get_length(self):
        count = 0;
        
        itr = self.head

        while itr:
            count +=1
            itr = itr.next

        return count
    
    # Remove at this index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index!")

        if index == 0:
            self.head = self.head.next  # python it self removes the garbage values
            return 

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # means at the previou element of the one which has to be deleted
                itr.next = itr.next.next    # removed
                break

            itr = itr.next
            count +=1

    # insert at the particular index
    def insert_atWithValue(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index!")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head

        while itr:
            
            if count == index - 1:      # before
                
                node = Node(data, itr.next)     # new node next is the next node of itr
                itr.next = node     # updating the link
                break

            itr = itr.next
            count += 1

    # insertion after a value
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            else:
                print("Value not found!")
                break
            itr = itr.next

    # Remove by value
    def remove_by_value(self, data):
        
        # if the list is empty
        if self.head is None:
            
            return

        # the value to be deleted is head
        if self.head.data == data:
            
            self.head = self.head.next
            return

        # if the value to be deleted is anywhere
        itr = self.head
        
        while itr.next:
            
            if itr.next.data == data:
                
                itr.next = itr.next.next
                break

            itr = itr.next
    
    # clear
    def clear(self):
        self.head = None

    def get_data(self):
        return self.head

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data   

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data)
    
    def linked_list_to_numpy_array(self):
        node = self.head
        values = []
        while node:
            values.append(node.data)
            node = node.next
        return np.array(values) 


if __name__ == "__main__":
   
    # ll = LinkedList()
    
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(89)
    # ll.insert_at_end(79)
    
    # ll.print()

    #######################################################

    lll = LinkedList()
    lll.insert_values(["Banana", "Mango", "Grapes", "Orange"])
    lll.remove_at(2)
    lll.insert_atWithValue(1, "jackfruit")
    lll.insert_after_value("Car", "Muhammad")
    lll.remove_by_value("Muhammad")
    lll.remove_by_value("Banana")
    lll.remove_by_value("Orange")
    print("Length: ", lll.get_length())
    lll.print()