import pytest
from stackQueuePseudo import Stack, PseudoQueue

@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def empty_pseudoqueue():
    return PseudoQueue()

def test_stack_push(empty_stack):
    empty_stack.push(1)
    assert not empty_stack.is_empty()

def test_stack_pop(empty_stack):
    empty_stack.push(1)
    item = empty_stack.pop()
    assert item == 1
    assert empty_stack.is_empty()

def test_stack_peek(empty_stack):
    empty_stack.push(1)
    item = empty_stack.peek()
    assert item == 1
    assert not empty_stack.is_empty()

def test_stack_is_empty(empty_stack):
    assert empty_stack.is_empty()

def test_pseudoqueue_enqueue(empty_pseudoqueue):
    empty_pseudoqueue.enqueue(1)
    assert not empty_pseudoqueue.stack1.is_empty()

def test_pseudoqueue_dequeue(empty_pseudoqueue):
    empty_pseudoqueue.enqueue(1)
    item = empty_pseudoqueue.dequeue()
    assert item == 1
    assert empty_pseudoqueue.stack1.is_empty()

def test_pseudoqueue_is_empty(empty_pseudoqueue):
    assert empty_pseudoqueue.stack1.is_empty()

