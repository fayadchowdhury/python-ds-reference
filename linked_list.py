# A linked list is a linear data structure in which elements may be stored in non-contiguous memory locations

import copy

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        # For doubly linked list
        # self.prev = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        # For doubly linked list
        # self.tail = tail
    
    def traverse(self):
        curr = self.head
        while ( curr != None):
            print(curr.data)
            curr = curr.next
        print("Reached end of list")
        return
    
    def length(self, node):
        curr = node
        if curr == None:
            return 0
        return self.length(curr.next) + 1
        
    
    def insert(self, node):
        curr = self.head
        if curr == None:
            curr = copy.deepcopy(node)
            self.head = curr
        else:
            while ( curr.next != None ):
                curr = curr.next
            curr.next = copy.deepcopy(node)
    
    def delete(self, value):
        curr = self.head
        prev = None
        while ( curr != None ):
            if curr.data == value:
                print("Found value. Deleting.")
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        print("Value not found in list :(")
    
    def reverse(self):
        curr = self.head
        prev = None
        next = None
        while ( curr != None ):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

def main():
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    
    ll = LinkedList()
    
    # first.next = second
    # second.next = third
    
    ll.insert(first)
    ll.insert(second)
    ll.insert(third)
    ll.insert(fourth)
    ll.insert(fourth)
    
    ll.traverse()
    
    ll.reverse()
    
    ll.traverse()
    
    ll.delete(6)
    ll.traverse()
main()