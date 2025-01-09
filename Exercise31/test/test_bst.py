import pytest

from Exercise31.binary_search_tree import BST


@pytest.fixture()
def tree_for_testing():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    return bst


def test_insert(tree_for_testing):
    bst = tree_for_testing

    assert bst.search(5) is True
    assert bst.search(3) is True
    assert bst.search(7) is True
    assert bst.search(10) is False


def test_search(tree_for_testing):
    bst = tree_for_testing

    assert bst.search(8) is True
    assert bst.search(5) is True
    assert bst.search(10) is False
    assert bst.search(2) is False


def test_delete_leaf(tree_for_testing):
    bst = tree_for_testing

    bst.delete(3)
    assert bst.search(3) is False
    assert bst.search(5) is True
    assert bst.search(8) is True


def test_delete_node_with_one_child(tree_for_testing):
    bst = tree_for_testing
    bst.delete(7)
    assert bst.search(7) is False
    assert bst.search(6) is True
    assert bst.search(5) is True


def test_delete_node_with_two_children(tree_for_testing):
    bst = tree_for_testing

    bst.delete(9)
    assert bst.search(9) is False
    assert bst.search(6) is True
    assert bst.search(8) is True
    assert bst.search(5) is True
