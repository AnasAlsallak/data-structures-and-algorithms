from hash.hash_table import HashTable
from trees import BinaryTree, Node

def tree_intersection(tree1, tree2):
    """
    Function that takes two binary tree parameters and returns a set of values found in both trees

    Args:
        tree1: A binary tree.
        tree2: A binary tree.
    
    Returns:
        A set of values found in both trees.
    """
    values = set()
    hashtable = HashTable()

    def traverse(node):

        if node:
            hashtable.set(str(node.value), node.value)

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

    traverse(tree1.root)

    def traverse2(node):

        if node:
            if hashtable.has(str(node.value)):
                values.add(node.value)

    traverse2(tree2.root)

    return values

if __name__ == "__main__":
    tree1 = BinaryTree()
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

    tree2 = BinaryTree()
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

    print(tree_intersection(tree1, tree2))

# Stretch Goal
# If the parameters were Binary Search Trees (BSTs) instead of generic binary trees, we can take advantage of the unique properties of BSTs to potentially solve the problem more efficiently.

# When dealing with BSTs, we can exploit the property that values to the left of a node are always smaller, and values to the right are always greater. This property allows us to perform an optimized traversal and comparison between the two BSTs.

# One approach to solving the intersection problem with BSTs could involve the following steps:

# 1. Traverse one BST (e.g., `tree1`) in an in-order manner and store the values in a set (`set1`).
#    - In-order traversal visits the nodes in ascending order, which aligns with the BST property.

# 2. Traverse the other BST (e.g., `tree2`) and check if each node's value is present in `set1`. If so, add it to the result set (`result`).

# 3. Return the `result` set, which contains the common values found in both BSTs.

# This approach leverages the property of BSTs to perform a more efficient intersection operation by avoiding unnecessary traversals. Instead of comparing each value in `tree2` with every value in `tree1`, we only need to check if the values from `tree2` are present in the `set1`.

# Potential Efficiency Differences:
# The potential efficiency differences between solving the intersection problem with generic binary trees and BSTs lie in the traversal and comparison steps:

# 1. Traversal: In the generic binary tree approach, a standard tree traversal (e.g., pre-order, in-order, post-order) is used. The time complexity for traversing a binary tree is O(n), where n is the number of nodes in the tree. In contrast, when working with BSTs, the in-order traversal is specifically utilized, which has a time complexity of O(n) as well.

# 2. Comparison: In the generic binary tree approach, a hash table is used to store the values from one tree, resulting in an additional space complexity of O(n). However, in the BST approach, a set (`set1`) is used instead, which only stores the unique values and has a space complexity of O(m), where m is the number of unique values in `tree1`.

# Overall, the potential efficiency difference lies in the space complexity. The BST approach may require less additional space due to utilizing a set instead of a hash table. However, the time complexity remains the same for both approaches, as they both involve traversing the trees once, resulting in a time complexity of O(n) in the worst case.

# It's worth noting that the efficiency differences become more prominent as the size of the trees increases, and the number of unique values in `tree1` becomes smaller compared to the total number of nodes. In such cases, the BST approach can provide improved efficiency by leveraging the BST properties and minimizing additional space requirements.
    