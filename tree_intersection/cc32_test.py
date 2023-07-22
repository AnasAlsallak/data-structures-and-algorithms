import pytest
from tree_intersection.tree_intersection import tree_intersection
from trees import BinaryTree, Node

def test_tree_intersection_happy_path():
    # Create two binary trees
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    # Populate tree1 with values
    tree1.root = Node(150)
    tree1.root.left = Node(100)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    tree1.root.right = Node(250)
    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(300)
    tree1.root.right.right.right = Node(500)

    # Populate tree2 with values
    tree2.root = Node(42)
    tree2.root.left = Node(100)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left = Node(125)
    tree2.root.left.right.right = Node(175)
    tree2.root.right = Node(600)
    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)
    tree2.root.right.right.left = Node(4)
    tree2.root.right.right.right = Node(500)

    # Expected intersection values: 100, 125, 160, 175, 200, 350, 500
    expected_intersection = {100, 125, 160, 175, 200, 350, 500}

    # Verify the intersection of the two binary trees
    assert tree_intersection(tree1, tree2) == expected_intersection


# Edge Case Test - Empty Trees
def test_tree_intersection_empty_trees():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    expected = set()
    assert tree_intersection(tree1, tree2) == expected

# Edge Case Test - One Tree is Empty
def test_tree_intersection_one_empty_tree():
    tree1 = BinaryTree()
    tree1.root = Node(150)
    tree1.root.left = Node(100)
    tree1.root.right = Node(200)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(125)

    tree2 = BinaryTree()
    expected = set()
    assert tree_intersection(tree1, tree2) == expected

# Expected Failure Test - Both Trees are None
def test_tree_intersection_both_trees_none():
    tree1 = None
    tree2 = None
    expected = set()
    assert tree_intersection(tree1, tree2) == expected
