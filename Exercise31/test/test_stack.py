import pytest

from Exercise31.Stack import Stack

@pytest.fixture()
def stack_for_testing():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

def test_push(stack_for_testing):
    stack = stack_for_testing

    assert stack.size() == 3


def test_pop(stack_for_testing):
    stack = stack_for_testing

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None


def test_size(stack_for_testing):
    stack = stack_for_testing

    assert stack.size() == 3
    stack.pop()
    assert stack.size() == 2
    stack.pop()
    assert stack.size() == 1
    stack.pop()
    assert stack.size() == 0


def test_is_empty():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    stack.push(2)
    assert stack.is_empty() is False
    stack.pop()
    stack.pop()
    assert stack.is_empty() is True

