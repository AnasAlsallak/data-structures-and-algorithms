import pytest
from arrayInsertShift import insertShiftArray
from arrayReverse import reverse_array
from arrayBinarySearch import binary_search
from linkedList import LinkedList
from linkedListInsertions import LinkedList

## first cc

def test_insertShiftArray():
    # Test case 1
    i_arr = [1, 2, 3, 4, 5]
    val = 6
    expected = [1, 2, 3, 6, 4, 5]
    o_arr = insertShiftArray(i_arr, val)
    assert o_arr == expected, f"Expected {expected}, but got {o_arr}"

    # Test case 2
    i_arr = [1, 2, 3, 4]
    val = 5
    expected = [1, 2, 5, 3, 4]
    o_arr = insertShiftArray(i_arr, val)
    assert o_arr == expected, f"Expected {expected}, but got {o_arr}"

    # Test case 3
    i_arr = []
    val = 1
    expected = [1]
    o_arr = insertShiftArray(i_arr, val)
    assert o_arr == expected, f"Expected {expected}, but got {o_arr}"
    
    # Test case 4
    i_arr = [1]
    val = 2
    expected = [1, 2]
    o_arr = insertShiftArray(i_arr, val)
    assert o_arr == expected, f"Expected {expected}, but got {o_arr}"

## second cc

def test_reverse_array():
    # Test case 1
    arr = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    o_arr = reverse_array(arr)
    assert o_arr == expected, f"Expected {expected}, but got {o_arr}"
    
    # Test case 2
    arr = [1, 2, 3, 4]
    expected = [4, 3, 2, 1]
    o_arr = reverse_array(arr)
    assert o_arr == expected, f"Expected {expected}, but got {o_arr}"
    
    # Test case 3
    arr = []
    expected = []
    o_arr = reverse_array(arr)
    assert o_arr == expected, f"Expected {expected}, but got {o_arr}"
    
    # Test case 4
    arr = [1]
    expected = [1]
    o_arr = reverse_array(arr)
    assert o_arr == expected, f"Expected {expected}, but got {o_arr}"

## third cc

def test_existing_target():
    arr = [2, 4, 6, 8, 10]
    target = 4
    assert binary_search(arr, target) == 1

def test_non_existing_target():
    arr = [2, 4, 6, 8, 10]
    target = 5
    assert binary_search(arr, target) == -1

def test_empty_array():
    arr = []
    target = 5
    assert binary_search(arr, target) == -1

def test_single_element_array():
    arr = [7]
    target = 7
    assert binary_search(arr, target) == 0

def test_target_at_leftmost_index():
    arr = [1, 3, 5, 7, 9]
    target = 1
    assert binary_search(arr, target) == 0

def test_target_at_rightmost_index():
    arr = [1, 3, 5, 7, 9]
    target = 9
    assert binary_search(arr, target) == 4

def test_duplicate_target():
    arr = [2, 4, 6, 6, 6, 8, 10]
    target = 6
    assert binary_search(arr, target) == 3

def test_large_input():
    arr = list(range(100000))
    target = 98765
    assert binary_search(arr, target) == 98765

## fifth cc

def test_linked_list():
    # Test empty linked list
    ll = LinkedList()
    assert ll.length == 0
    assert ll.to_string() == "NONE"

    # Test insert into linked list
    ll.insert(10)
    assert ll.length == 1
    assert ll.to_string() == "{ 10 } -> NONE"

    # Test head property points to first node
    assert ll.head.value == 10

    # Test insert multiple nodes
    ll.insert(20)
    ll.insert(30)
    assert ll.length == 3
    assert ll.to_string() == "{ 30 } -> { 20 } -> { 10 } -> NONE"

    # Test finding value in linked list
    assert ll.includes(20) == True
    assert ll.includes(40) == False

    # Test returning collection of all values
    values = ll.get_values()
    assert values == [30, 20, 10]

## sixth cc 

def test_append():
    ll = LinkedList()
    assert ll.length == 0
    ll.append(1)
    assert ll.length == 1
    assert ll.head.value == 1
    ll.append(2)
    assert ll.length == 2
    assert ll.head.next.value == 2
    ll.append(3)
    assert ll.length == 3
    assert ll.head.next.next.value == 3


def test_insert_before_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, "new_value")
    assert ll.head.next.value == "new_value"
    assert ll.head.next.next.value == 2


def test_insert_before_first():
    ll = LinkedList()
    ll.append(1)
    ll.insert_before(1, "new_value")
    assert ll.head.value == "new_value"
    assert ll.head.next.value == 1


def test_insert_after_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, "new_value")
    assert ll.head.next.next.value == "new_value"
    assert ll.head.next.next.next.value == 3


def test_insert_after_last():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.insert_after(2, "new_value")
    assert ll.head.next.next.value == "new_value"
    assert ll.head.next.next.next is None





    
