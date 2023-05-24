# Code Challenge: Class 15

Write out code as part of your whiteboard process.

## Feature Tasks

- Features
- Node
    -Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- Binary Tree
    - Create a Binary Tree class
        - Define a method for each of the depth first traversals:
            - pre order
            - in order
            - post order
    - Each depth first traversal method should return an array of values, ordered appropriately.
- Binary Search Tree
    - Create a Binary Search Tree class
        - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
        - Add
            - Arguments: value
            - Return: nothing
            - Adds a new node with that value in the correct location in the binary search tree.
        - Contains
            - Argument: value
            - Returns: boolean  indicating whether or not the value is in the tree at least once.

## Stretch Goal

Create a new branch called k-ary-tree, and, using the resources available to you online, implement a k-ary tree, where each node can have any number of children.

## Approach & Efficiency

Using of the deque class and its methods, conditionals, loops.

In both methods, the time complexity is O(1) because the operations performed, such as appending to a deque, comparing timestamps, and removing elements, have constant time complexities.

The space complexity is also O(1) as the amount of additional space used does not depend on the input size and remains constant.

## Solution

[Code](../trees.py)

[Tests](../tests/cc15_test.py)

![Run](../assets/run12.JPG "run")

[Move to CC 16](..//README.md) | [Previous](..//README.md)
