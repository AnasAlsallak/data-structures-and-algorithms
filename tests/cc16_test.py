import pytest
from treeMax import Node, BinaryTree

# an empty binary tree (expected failure)
def test_get_max_empty_tree():
    tree = BinaryTree()
    with pytest.raises(Exception):
        tree.get_max()

# a binary tree with only one node
def test_get_max_single_node():
    tree = BinaryTree()
    tree.root = Node(5)
    assert tree.get_max() == 5

# a binary tree with positive values
def test_get_max_positive_values():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(20)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(8)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(25)
    assert tree.get_max() == 25

# a binary tree with negative values
def test_get_max_negative_values():
    tree = BinaryTree()
    tree.root = Node(-10)
    tree.root.left = Node(-5)
    tree.root.right = Node(-20)
    tree.root.left.left = Node(-3)
    tree.root.left.right = Node(-8)
    tree.root.right.left = Node(-15)
    tree.root.right.right = Node(-25)
    assert tree.get_max() == -3

# a binary tree with a mix of positive and negative values
def test_get_max_mixed_values():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(-3)
    tree.root.right = Node(8)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(-7)
    tree.root.right.left = Node(12)
    tree.root.right.right = Node(4)
    assert tree.get_max() == 12

# a binary tree with duplicate maximum values
def test_get_max_duplicate_max_values():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(20)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(8)
    tree.root.right.left = Node(20)
    tree.root.right.right = Node(25)
    assert tree.get_max() == 25
