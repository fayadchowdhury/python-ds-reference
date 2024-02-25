# Import double-ended queue
from collections import deque

# Implement queue data structure

class Queue():
    def __init__(self):
        self._elements = deque()
        
    def __len__(self):
        return len(self._elements)
    
    def __iter__(self): # Require better understanding of this
        self._elements_copy = self._elements.copy()
        while len(self._elements_copy) > 0:
            yield self._elements_copy.popleft()
        
    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        if len(self._elements) > 0:
            return self._elements.popleft()
        else:
            print("No item in queue :(")
    
    def front(self):
        if len(self._elements) > 0:
            front =  self._elements.popleft()
            self._elements.appendleft(front)
            return front
        else:
            print("No item in queue :(")

class Stack():
    def __init__(self):
        self._elements = deque()
        
    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        self._elements_copy = self._elements.copy()
        while len(self._elements_copy) > 0:
            yield self._elements_copy.pop()
    
    def empty(self):
        return len(self._elements) == 0
    
    def top(self):
        if len(self._elements) > 0:
            top = self._elements.pop()
            self._elements.append(top)
            return top
        else:
            print("No item in stack :(")
    
    def push(self, element):
        self._elements.append(element)
        
    def pop(self):
        if len(self._elements) > 0:
            return self._elements.pop()
        else:
            print("No item in stack :(")

def main():
    # queue = Queue()
    # queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # for elem in queue:
    #     print(elem)
    # print(queue.dequeue())
    # print(queue.front())
    
    s = Stack()
    print(s.empty()) # True
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.empty()) # False
    print(len(s))
    for elem in s:
        print(elem)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())    
    
main()