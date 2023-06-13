import pytest
from typing import List
from sorting import Insert, InsertionSort

# Happy path test for Insert function
def test_insert_happy():
    sorted_list = [1, 3, 5, 7]
    value = 4
    Insert(sorted_list, value)
    assert sorted_list == [1, 3, 4, 5, 7]

# Expected failure test for Insert function
@pytest.mark.xfail
def test_insert_failure():
    sorted_list = [1, 3, 5, 7]
    value = 7
    with pytest.raises(IndexError):
        Insert(sorted_list, value)

# Edge cases test for Insert function
def test_insert_edge_cases():
    # Empty sorted list
    sorted_list = []
    value = 5
    Insert(sorted_list, value)
    assert sorted_list == [5]

def test_insert_edge_cases_2():

    # Value smaller than all elements in the sorted list
    sorted_list = [3, 6, 9]
    value = 1
    Insert(sorted_list, value)
    assert sorted_list == [1, 3, 6, 9]

def test_insert_edge_cases_3():

    # Value larger than all elements in the sorted list
    sorted_list = [2, 4, 6, 8]
    value = 10
    Insert(sorted_list, value)
    assert sorted_list == [2, 4, 6, 8, 10]

# Happy path test for InsertionSort function
def test_insertion_sort_happy():
    input_list = [4, 2, 7, 1, 5]
    sorted_output = InsertionSort(input_list)
    assert sorted_output == [1, 2, 4, 5, 7]

# Expected failure test for InsertionSort function
@pytest.mark.xfail
def test_insertion_sort_failure():
    input_list = []
    sorted_output = InsertionSort(input_list)
    assert sorted_output == []

# Edge cases test for InsertionSort function
def test_insertion_sort_edge_cases():
    # Single-element list
    input_list = [9]
    sorted_output = InsertionSort(input_list)
    assert sorted_output == [9]

def test_insertion_sort_edge_cases_2():

    # List with all elements equal
    input_list = [2, 2, 2, 2]
    sorted_output = InsertionSort(input_list)
    assert sorted_output == [2, 2, 2, 2]

def test_insertion_sort_edge_cases_3():

    # Already sorted list
    input_list = [1, 2, 3, 4, 5]
    sorted_output = InsertionSort(input_list)
    assert sorted_output == [1, 2, 3, 4, 5]

def test_insertion_sort_edge_cases_4():

    # List in descending order
    input_list = [5, 4, 3, 2, 1]
    sorted_output = InsertionSort(input_list)
    assert sorted_output == [1, 2, 3, 4, 5]

def test_insertion_sort_edge_cases_5():

    # List with negative numbers
    input_list = [-4, -1, -7, -2, -5]
    sorted_output = InsertionSort(input_list)
    assert sorted_output == [-7, -5, -4, -2, -1]
