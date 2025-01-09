import pytest

from Exercise31.Queue import Queue

@pytest.fixture()
def queue_for_testing():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q

def test_enqueue(queue_for_testing):
    q = queue_for_testing

    assert q.size() == 3


def test_dequeue(queue_for_testing):
    q = queue_for_testing

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.size() == 0


def test_is_empty():
    q = Queue()
    assert q.is_empty() is True
    q.enqueue(1)
    assert q.is_empty() is False
    q.dequeue()
    assert q.is_empty() is True
