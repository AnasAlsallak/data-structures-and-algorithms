# Code Challenge: Class 11

Write out code as part of your whiteboard process.

## Feature Tasks

Create a new class called pseudo queue.
    - Do not use an existing Queue.
    - Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
    - Internally, utilize 2 Stack instances to create and manage the queue
Methods:
    - enqueue
        - Arguments: value
        - Inserts a value into the PseudoQueue, using a first-in, first-out approach.
    - dequeue
        - Arguments: none
        - Extracts a value from the PseudoQueue, using a first-in, first-out approach.
**NOTE:** The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Approach & Efficiency

The time complexity of the enqueue and dequeue operations in this implementation is O(n), where n is the number of elements in the PseudoQueue. This is because in the enqueue operation, we need to move all elements from stack1 to stack2 (n operations), and in the dequeue operation, we simply pop from stack1 (1 operation). The while loops for moving elements between the stacks contribute to the linear time complexity.

The space complexity of the PseudoQueue implementation is O(n), where n is the number of elements in the PseudoQueue. This is because we are using two Stack objects, stack1 and stack2, to simulate the queue behavior. The space required will grow linearly with the number of elements in the PseudoQueue.

## Solution

[Code](../stackQueuePseudo.py)

[Tests](../tests/cc11_test.py)

![Run](../assets/run10.JPG "run")

[Move to CC 12](..//README.md) | [Previous](../stack_and_queue/README.md)
