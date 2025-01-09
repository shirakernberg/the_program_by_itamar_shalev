from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self.queue: list[T] = []

    def enqueue(self, value: T):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

