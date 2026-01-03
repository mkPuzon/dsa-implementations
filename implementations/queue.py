'''
Implements a queue data structure in Python.

Jan 2025
'''

class Queue:
    '''A general queue class to store any kind of object.'''

    def __init__(self):
        self._queue = []
        self._num_items = 0
    
    def peek(self) -> object:
        if self._num_items == 0:
            return None
        return self._queue[0]
    
    def enqueue(self, item: object) -> None:
        self._queue.append(item)
        self._num_items += 1
    
    def dequeue(self) -> object:
        if self._num_items == 0:
            return None
        self._num_items -= 1
        return self._queue.pop(0)
    
    def size(self) -> int:
        return self._num_items
    
    def is_empty(self) -> bool:
        return self._num_items == 0

    def __repr__(self) -> str:
        next_item = self.peek()
        next_str = f", next={next_item}" if next_item else ""
        return f"Queue(size={self._num_items}{next_str})"