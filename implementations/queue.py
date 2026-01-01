'''
Implements a queue data structure in Python.

Jan 2025
'''

class Queue:
    '''A general queue class to store any kind of object.'''

    def __init__(self):
        self._queue = []
        self.size = 0
    
    def peek(self) -> object:
        if self.size == 0:
            return None
        return self._queue[0]
    
    def enqueue(self, item: object) -> None:
        self._queue.append(item)
        self.size += 1
    
    def dequeue(self) -> object:
        self.size -= 1
        return self._queue.pop(index=0)
    
    def size(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return self.size == 0

    def __str__(self) -> str:
        return f"Queue with {self.size} elements. From first in to last in:\n{self._queue}"