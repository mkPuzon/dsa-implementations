'''
Custom Python implementations of min and max heaps.

Jan 2026
'''
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable, Optional

T = TypeVar("T")

class Heap(Generic[T], ABC):

    # prevents accidental attribute creation and optimizes memory
    __slots__ = ("_data", "_key", "_size")

    def __init__(self, key: Callable[[T], object] | None = None):
        '''Allows selection of comparision function or attribute; works with custom classes.'''
        self._key: Callable = key or (lambda x: x)
        self._size: int = 0 
        self._data: list[T] = [] 

    def peek(self) -> Optional[T]:
        if self._size == 0:
            return None
        return self._data[0]
    
    @abstractmethod
    def _compare(self, a: T, b: T) -> bool:
        pass
    
    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def pushpop(self, item: T) -> T:
        pass

    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        top = self.peek()
        top_str = f", top={top}" if top else ""
        return f"{self.__class__.__name__}(size={self._size}{top_str}, key={self._key})"

    def __bool__(self) -> bool:
        return self._data

    def __contains__(self, item: T) -> bool:
        # TODO
        pass

    def __iter__(self) -> T:
        # TODO
        pass


class MinHeap(Heap):
    
    def _compare(self, a: T, b: T):
        return self._key(a) < self._key(b)


class MaxHeap(Heap):
    
    def _compare(self, a: T, b: T):
        return self._key(a) > self._key(b)