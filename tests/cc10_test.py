from stackAndQueue import Stack, Queue

# Testing the Stack class
def test_stack_functionality():
    stack = Stack()
    # Test pushing an item onto a stack
    stack.push(10)
    assert stack.peek() == 10

    # Test pushing multiple values onto a stack
    stack.push(20)
    stack.push(30)
    assert stack.peek() == 30

    # Test popping off the stack
    assert stack.pop() == 30

    # Test emptying a stack after multiple pops
    stack.pop()
    stack.pop()
    assert stack.is_empty()

    # Test peeking the next item on the stack
    stack.push(40)
    assert stack.peek() == 40

    # Test instantiating an empty stack
    empty_stack = Stack()
    assert empty_stack.is_empty()

    # Test calling pop or peek on empty stack raises exception
    try:
        empty_stack.pop()
        # The following line should not be reached
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "Stack is empty"

    try:
        empty_stack.peek()
        # The following line should not be reached
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "Stack is empty"


# Testing the Queue class
def test_queue_functionality():
    queue = Queue()

    # Test enqueueing into a queue
    queue.enqueue(10)
    assert queue.peek() == 10

    # Test enqueueing multiple values into a queue
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.peek() == 10

    # Test dequeuing out of a queue the expected value
    assert queue.dequeue() == 10

    # Test peeking into a queue, seeing the expected value
    assert queue.peek() == 20

    # Test emptying a queue after multiple dequeues
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()

    # Test instantiating an empty queue
    empty_queue = Queue()
    assert empty_queue.is_empty()

    # Test calling dequeue or peek on empty queue raises exception
    try:
        empty_queue.dequeue()
        # The following line should not be reached
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "Queue is empty"

    try:
        empty_queue.peek()
        # The following line should not be reached
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "Queue is empty"
