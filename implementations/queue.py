'''
Implements a queue data structure in Python.

Jan 2025
'''

class Queue:
    '''A general queue class to store any kind of object.'''

    def __init__(self):
        self._queue = []
        self.num_items = 0
    
    def peek(self) -> object:
        if self.num_items == 0:
            return None
        return self._queue[0]
    
    def enqueue(self, item: object) -> None:
        self._queue.append(item)
        self.num_items += 1
    
    def dequeue(self) -> object:
        if self.num_items == 0:
            return None
        self.num_items -= 1
        return self._queue.pop(0)
    
    def size(self) -> int:
        return self.num_items
    
    def is_empty(self) -> bool:
        return self.num_items == 0

    def __str__(self) -> str:
        return f"Queue with {self.num_items} elements. From first in to last in:\n{self._queue}"