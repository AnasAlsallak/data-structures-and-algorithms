# Code Challenge 36: Implementation: Hash Tables

Write the following method for the Graph class:

- breadth first:
    Arguments: Node
    Return: A collection of nodes in the order they were visited.
    Display the collection

## Whiteboard

![Whiteboard36](/assets/Wireframe36.jpg "Whiteboard36")

## Approach & Efficiency

Classes, loops, conditionals.

Time Complexity: O(V + E) as the time complexity of BFS is determined by the sum of all the vertices' degrees and the number of vertices

Space Complexity: O(V) as it requires a set to store visited vertices, and the queue can have at most V elements in it during the traversal.

## Solution

![run 36](/assets/run36.JPG "run example")

test:

![test 36](/assets/test36.JPG "test")
