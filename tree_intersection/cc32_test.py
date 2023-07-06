import pytest
from tree_intersection import tree_intersection
from trees import BinaryTree, Node

# Example test cases
@pytest.fixture
def setup_trees():
    # Create two binary trees
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    # Populate tree1
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree1.root.right.left = Node(6)
    tree1.root.right.right = Node(7)

    # Populate tree2
    tree2.root = Node(3)
    tree2.root.left = Node(5)
    tree2.root.right = Node(7)
    tree2.root.left.left = Node(8)
    tree2.root.left.right = Node(9)

    return tree1, tree2

def test_tree_intersection_happy_path(setup_trees):
    tree1, tree2 = setup_trees
    expected = {3, 5, 7}
    assert tree_intersection(tree1, tree2) == expected

def test_tree_intersection_empty_tree(setup_trees):
    tree1 = BinaryTree()  # Empty tree
    tree2 = setup_trees
    expected = set()
    assert tree_intersection(tree1, tree2) == expected

def test_tree_intersection_no_common_values(setup_trees):
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.root = Node(1)
    tree2.root = Node(2)
    expected = set()
    assert tree_intersection(tree1, tree2) == expected

def test_tree_intersection_same_tree(setup_trees):
    tree1, _ = setup_trees
    expected = {1, 2, 3, 4, 5, 6, 7}
    assert tree_intersection(tree1, tree1) == expected

def test_tree_intersection_missing_tree():
    tree1 = BinaryTree()
    tree2 = None
    expected = set()
    assert tree_intersection(tree1, tree2) == expected

def test_tree_intersection_missing_values(setup_trees):
    tree1, tree2 = setup_trees
    tree2.root = None
    expected = set()
    assert tree_intersection(tree1, tree2) == expected
