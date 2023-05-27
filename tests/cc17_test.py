import pytest
from trees import BinaryTree, Node
from treeBreadthFirst import tree_breadth_first

# edge case
def test_empty_tree():
    tree = BinaryTree()
    assert tree_breadth_first(tree) == []

# edge case
def test_single_node_tree():
    tree = BinaryTree()
    tree.root = Node(1)
    assert tree_breadth_first(tree) == [1]


def test_random_tree():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(6)
    assert tree_breadth_first(tree) == [1, 2, 3, 4, 5, 6]


def test_tree_with_only_left_children():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.left.left = Node(4)
    assert tree_breadth_first(tree) == [1, 2, 3, 4]


def test_tree_with_only_right_children():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.right = Node(2)
    tree.root.right.right = Node(3)
    tree.root.right.right.right = Node(4)
    assert tree_breadth_first(tree) == [1, 2, 3, 4]


def test_tree_with_single_level():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    assert tree_breadth_first(tree) == [1, 2, 3]


def test_tree_with_two_levels():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.right.right = Node(5)
    assert tree_breadth_first(tree) == [1, 2, 3, 4, 5]


def test_tree_with_unbalanced_levels():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.right.left.left = Node(6)
    assert tree_breadth_first

# expected failure

def test_tree_with_invalid_node():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = "Invalid"
    tree.root.left.left = Node(4)

    with pytest.raises(AttributeError):
        tree_breadth_first(tree)


