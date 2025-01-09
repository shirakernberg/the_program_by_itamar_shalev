from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Heap(Generic[T]):
    def __init__(self, is_min_heap=True):
        self.heap: list[T] = []
        self.is_min_heap = is_min_heap

    def compare(self, value1: T, value2: T) -> bool:
        return value1 < value2 if self.is_min_heap else value1 > value2

    def push(self, value: T) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) -> Optional[T]:
        if len(self.heap) == 0:
            return

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self) -> Optional[T]:
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def _heapify_up(self, index: int) -> None:
        parent = (index - 1) // 2

        while index > 0 and self.compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index) -> None:
        n = len(self.heap)
        while True:
            smallest_or_largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < n and self.compare(self.heap[left], self.heap[smallest_or_largest]):
                smallest_or_largest = left
            if right < n and self.compare(self.heap[right], self.heap[smallest_or_largest]):
                smallest_or_largest = right
            if smallest_or_largest == index:
                break
            self.heap[index], self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[index]
            index = smallest_or_largest

    def is_empty(self) -> bool:
        return len(self.heap) == 0
