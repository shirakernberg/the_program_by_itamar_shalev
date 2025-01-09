from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T):
        self.val = value
        self.next = None


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, value: T) -> None:
        new_node: Optional[Node] = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last: Optional[Node] = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self) -> None:
        cur_node = self.head
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next

    def insert_front(self, value) -> None:
        new_node: Node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node_val: T, value: T) -> None:
        prev_node = self.search(prev_node_val)
        if prev_node is None:
            return None

        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, value) -> None:
        cur_node = self.head
        if cur_node and cur_node.val == value:
            self.head = cur_node.next
            return

        prev = None
        while cur_node and cur_node.val != value:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next

    def search(self, value) -> Optional[Node]:
        cur_node = self.head
        while cur_node:
            if cur_node.val == value:
                return cur_node
            cur_node = cur_node.next
        return None
