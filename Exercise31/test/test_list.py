import pytest

from Exercise31.linked_list import LinkedList

@pytest.fixture()
def linked_list_for_testing():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    return ll

def test_append(linked_list_for_testing):
    ll = linked_list_for_testing

    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 3
    assert ll.head.next.next.next is None


def test_insert_front():
    ll = LinkedList()
    ll.insert_front(1)
    ll.insert_front(2)
    ll.insert_front(3)

    assert ll.head.val == 3
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 1
    assert ll.head.next.next.next is None


def test_insert(linked_list_for_testing):
    ll = linked_list_for_testing

    ll.insert(2, 4)
    assert ll.head.val == 1
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 4
    assert ll.head.next.next.next.val == 3
    assert ll.head.next.next.next.next is None


def test_delete(linked_list_for_testing):
    ll = linked_list_for_testing

    ll.delete(2)
    assert ll.head.val == 1
    assert ll.head.next.val == 3
    assert ll.head.next.next is None


def test_search(linked_list_for_testing):
    ll = linked_list_for_testing

    assert ll.search(2).val == 2
    assert ll.search(4) is None
    assert ll.search(1).val == 1
    assert ll.search(5) is None
    assert ll.search(3).val == 3
