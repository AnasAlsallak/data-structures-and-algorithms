# Code Challenge: Class 13

Write out code as part of your whiteboard process.

## Feature Tasks

- Write a function called validate brackets
- Arguments: string
- Return: boolean
  - representing whether or not the brackets in the string are balanced
- There are 3 types of brackets:

  - Round Brackets : ()
  - Square Brackets : []
  - Curly Brackets : {}

## Whiteboard Process

![Whiteboard 15](../assets/Wireframe-15.jpg "whiteboard")

## Approach & Efficiency

Using of stack class and its methods, conditionals, loops.

In both methods, the time complexity is O(1) because the operations performed, such as appending to a deque, comparing timestamps, and removing elements, have constant time complexities.

The space complexity is also O(1) as the amount of additional space used does not depend on the input size and remains constant.

## Solution

[Code](../stackQueueBrackets.py)

[Tests](../tests/cc13_test.py)

![Run](../assets/run13.JPG "run")

[Move to CC 14](..//README.md) | [Previous](../stack-queue-animal-shelter/README.md)
