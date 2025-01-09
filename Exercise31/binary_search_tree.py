from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None


def _min_value_node(node: Optional[Node[T]]) -> Node[T]:
    current = node
    while current.left is not None:
        current = current.left
    return current


class BST(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None

    def insert(self, data: T):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node: Node[T], value: T):
        if value < node.val:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value: T) -> bool:
        return self._search(self.root, value)

    def _search(self, node: Optional[Node[T]], value: T) -> bool:

        if node is None:
            return False
        if node.val == value:
            return True
        if value < node.val:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def delete(self, delete_value: T):
        self.root = self._delete(self.root, delete_value)

    def _delete(self, node: Optional[Node[T]], delete_value: T) -> Optional[Node[T]]:
        if node is None:
            return None
        if delete_value < node.val:
            node.left = self._delete(node.left, delete_value)
        elif delete_value > node.val:
            node.right = self._delete(node.right, delete_value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = _min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node: Optional[Node[T]]):
        if node is not None:
            self._inorder(node.left)
            print(node.val, end=' ')
            self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node: Optional[Node]):
        if node is not None:
            print(node.val, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node: Optional[Node]):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val, end=' ')


def main():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    bst.inorder()
    print()
    bst.preorder()
    print()
    bst.postorder()
    print()


main()
