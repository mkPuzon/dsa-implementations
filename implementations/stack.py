'''
Implements a stack data structure in Python.

Jan 2026
'''

class Stack:
    '''A general stack class to store any kind of objects.'''

    def __init__(self) -> None:
        self._stack = []
        self._num_items = 0
        
    def add(self, val: object) -> None:
        self._stack.append(val)
        self._num_items += 1
    
    def peek(self) -> object:
        if self._num_items == 0:
            return None
        return self._stack[-1]
    
    def pop(self) -> object:
        if self._num_items == 0:
            return None
        self._num_items -= 1
        return self._stack.pop()
    
    def is_empty(self) -> bool:
        return self._num_items == 0
    
    def size(self) -> int:
        return self._num_items
    
    def __repr__(self) -> str:
        top = self.peek()
        top_str = f", top={top}" if top else ""
        return f"Stack(size={self._num_items}{top_str})"

if __name__ == "__main__":
    s = Stack()
    print(s)
    s.add(2)
    s.add("hello")
    s.add(15.3)
    print(s.peek())
    s.pop()
    s.pop()
    print(s.peek())
    s.add(4)
    print(s)