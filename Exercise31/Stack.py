from typing import TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.stack: list[T] = []

    def push(self, value: T):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0
