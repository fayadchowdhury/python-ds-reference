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
        return self._elements.popleft()
    
    def front(self):
        front =  self._elements.popleft()
        self._elements.appendleft(front)
        return front

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    for elem in queue:
        print(elem)
    print(queue.dequeue())
    print(queue.front())
    
main()