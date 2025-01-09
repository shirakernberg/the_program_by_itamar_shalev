import pytest

from Exercise31.Heap import Heap

@pytest.fixture()
def heap_for_testing():
    heap = Heap()
    heap.push(3)
    heap.push(1)
    heap.push(5)
    heap.push(0)
    heap.push(2)
    heap.push(4)
    return heap

def test_min_heap(heap_for_testing):
    heap = heap_for_testing

    assert heap.pop() == 0
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert heap.pop() == 4
    assert heap.pop() == 5


def test_max_heap():
    heap = Heap(is_min_heap=False)
    heap.push(3)
    heap.push(1)
    heap.push(5)
    heap.push(0)
    heap.push(2)
    heap.push(4)

    assert heap.pop() == 5
    assert heap.pop() == 4
    assert heap.pop() == 3
    assert heap.pop() == 2
    assert heap.pop() == 1
    assert heap.pop() == 0


def test_peek(heap_for_testing):
    heap = heap_for_testing

    assert heap.peek() == 0
    heap.pop()
    assert heap.peek() == 1
    heap.pop()
    assert heap.peek() == 2
    heap.pop()
    assert heap.peek() == 3
    heap.pop()
    assert heap.peek() == 4
    heap.pop()
    assert heap.peek() == 5


def test_is_empty():
    heap = Heap()
    assert heap.is_empty() is True
    heap.push(1)
    assert heap.is_empty() is False
