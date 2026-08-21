class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self , data):          #Insert at end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = new_node
    def insertatbegin(self , data):    # insert at begin
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        self.head =   new_node
        self.head.next = current 
    
    def delatbegin(self):                   # deelete at begining
        if self.head is None :
            return
        current = self.head
        self.head = current.next

    def delatend(self):                     # delete at end
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        previous = self.head
        current = previous.next
        while current.next:
            previous = previous.next
            current = current.next
        previous.next = None
    def display(self):                  # traverse the list
        current = self.head
        
        while current:
            print(current.data , end ="->")
            current = current.next
        print("None")

l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.delatend()
l1.display()