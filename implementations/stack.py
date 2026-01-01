'''
Implements a stack data structure in Python.

Jan 2026
'''

class Stack:
    '''A general stack class to store any kind of objects.'''

    def __init__(self) -> None:
        self._stack = []
        self.num_items = 0
        
    def add(self, val: object) -> None:
        self._stack.append(val)
        self.num_items += 1
    
    def peek(self) -> object:
        if self.num_items == 0:
            return None
        return self._stack[-1]
    
    def pop(self) -> object:
        if self.num_items == 0:
            return None
        return self._stack.pop()

    def get_num_items(self):
        return self.num_items
    
    def __str__(self):
        return f"Stack contains {self.num_items} items. From bottom to top:\n{self._stack}"


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