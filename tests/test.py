import pytest
from arrayInsertShift import insertShiftArray
from arrayReverse import reverse_array

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

    
