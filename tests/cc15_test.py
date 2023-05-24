import pytest
from trees import BinaryTree, BinarySearchTree, Node

def test_instantiate_empty_tree():
    tree = BinaryTree()
    assert tree.root is None

def test_instantiate_tree_with_root_node():
    tree = BinaryTree()
    tree.root = Node(1)
    assert tree.root.value == 1

def test_add_left_right_child_to_binary_search_tree():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)
    assert bst.root.value == 4
    assert bst.root.left.value == 2
    assert bst.root.right.value == 6

def test_preorder():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    assert tree.preorder(tree.root) == [1, 2, 4, 5, 3]

def test_inorder():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    assert tree.inorder(tree.root) == [4, 2, 5, 1, 3]

def test_postorder():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    assert tree.postorder(tree.root) == [4, 5, 2, 3, 1]

def test_contains_existing_value_in_binary_search_tree():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)
    assert bst.contains(2) is True

def test_contains_nonexisting_value_in_binary_search_tree():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)
    assert bst.contains(5) is False
    
@pytest.mark.xfail
def test_contains_empty_binary_search_tree():
    bst = BinarySearchTree()
    assert bst.contains(1) is False

@pytest.mark.xfail
def test_contains_value_in_empty_binary_search_tree():
    bst = BinarySearchTree()
    with pytest.raises(ValueError):
        bst.contains(2)
   
