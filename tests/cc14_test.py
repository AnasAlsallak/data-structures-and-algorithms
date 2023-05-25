import pytest
from stackGetMax import Stack

#  an empty stack
def test_get_max_empty_stack():
    stack = Stack()
    with pytest.raises(Exception, match="Stack is empty"):
        stack.get_max()

#  a stack with one element
def test_get_max_single_element():
    stack = Stack()
    stack.push(5)
    assert stack.get_max() == 5

#  a stack with multiple elements
def test_get_max_multiple_elements():
    stack = Stack()
    stack.push(3)
    stack.push(8)
    stack.push(2)
    stack.push(5)
    assert stack.get_max() == 8

# repeated maximum values
def test_get_max_repeated_max():
    stack = Stack()
    stack.push(5)
    stack.push(8)
    stack.push(8)
    stack.push(2)
    assert stack.get_max() == 8

# popping the maximum value from the stack
def test_get_max_after_pop():
    stack = Stack()
    stack.push(3)
    stack.push(8)
    stack.push(2)
    stack.push(5)
    stack.pop()
    assert stack.get_max() == 8

# pushing a larger value onto the stack
def test_get_max_push_larger_value():
    stack = Stack()
    stack.push(3)
    stack.push(8)
    stack.push(2)
    stack.push(5)
    stack.push(10)
    assert stack.get_max() == 10

# get_max() on an empty stack (expected failure)
def test_get_max_empty_stack():
    stack = Stack()
    with pytest.raises(Exception, match="Stack is empty"):
        stack.get_max()

# a stack with negative values (edge case)
def test_get_max_negative_values():
    stack = Stack()
    stack.push(-5)
    stack.push(-2)
    stack.push(-8)
    assert stack.get_max() == -2

# a stack with all equal values (edge case)
def test_get_max_all_equal_values():
    stack = Stack()
    stack.push(5)
    stack.push(5)
    stack.push(5)
    assert stack.get_max() == 5

# a stack with only one element and negative value (edge case)
def test_get_max_single_negative_value():
    stack = Stack()
    stack.push(-10)
    assert stack.get_max() == -10

#  a stack with a large number of elements (edge case)
def test_get_max_large_stack():
    stack = Stack()
    for i in range(100000):
        stack.push(i)
    assert stack.get_max() == 99999


