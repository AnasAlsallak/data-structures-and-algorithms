import pytest
from linkedList import LinkedList
from linkedListInsertions import LinkedList
from linkedListKth import LinkedList
from linkedListZip import LinkedList

def test_zip_lists():
    # Test case with both lists having the same length
    list_a = LinkedList()
    list_b = LinkedList()
    list_a.append(1)
    list_a.append(3)
    list_a.append(5)
    list_b.append(2)
    list_b.append(4)
    list_b.append(6)
    expected_result = [1, 2, 3, 4, 5, 6]
    result = LinkedList.linkedListZip(list_a, list_b)
    assert result.get_values() == expected_result

    # Test case with list_a being longer than list_b
    list_a = LinkedList()
    list_b = LinkedList()
    list_a.append(1)
    list_a.append(3)
    list_a.append(5)
    list_a.append(7)
    list_b.append(2)
    list_b.append(4)
    expected_result = [1, 2, 3, 4, 5, 7]
    result = LinkedList.linkedListZip(list_a, list_b)
    assert result.get_values() == expected_result

    # Test case with list_b being longer than list_a
    list_a = LinkedList()
    list_b = LinkedList()
    list_a.append(1)
    list_a.append(3)
    list_b.append(2)
    list_b.append(4)
    list_b.append(6)
    list_b.append(8)
    expected_result = [1, 2, 3, 4, 6, 8]
    result = LinkedList.linkedListZip(list_a, list_b)
    assert result.get_values() == expected_result

    # Test case with an empty list_a
    list_a = LinkedList()
    list_b = LinkedList()
    list_b.append(2)
    list_b.append(4)
    list_b.append(6)
    expected_result = [2, 4, 6]
    result = LinkedList.linkedListZip(list_a, list_b)
    assert result.get_values() == expected_result

    # Test case with an empty list_b
    list_a = LinkedList()
    list_a.append(1)
    list_a.append(3)
    list_a.append(5)
    list_b = LinkedList()
    expected_result = [1, 3, 5]
    result = LinkedList.linkedListZip(list_a, list_b)
    assert result.get_values() == expected_result

    # Test case with both empty lists
    list_a = LinkedList()
    list_b = LinkedList()
    expected_result = []
    result = LinkedList.linkedListZip(list_a, list_b)
    assert result.get_values() == expected_result

    # Test case with a single element in each list
    list_a = LinkedList()
    list_b = LinkedList()
    list_a.append(1)
    list_b.append(2)
    expected_result = [1, 2]
    result = LinkedList.linkedListZip(list_a, list_b)
    assert result.get_values() == expected_result

    # Test case with one list being None
    list_a = LinkedList()
    list_b = None
    list_a.append(1)
    list_a.append(3)
    list_a.append(5)
    expected_result = [1, 3, 5]
    result = LinkedList.linkedListZip(list_a, list_b)
    assert result.get_values() == expected_result
