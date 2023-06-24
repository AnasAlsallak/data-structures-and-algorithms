import pytest
from typing import List
from merge_sort import merge_sort

@pytest.fixture
def unsorted_list() -> List[int]:
    return [8, 4, 23, 42, 16, 15]

@pytest.fixture
def sorted_list() -> List[int]:
    return [4, 8, 15, 16, 23, 42]

def test_merge_sort_happy_path(unsorted_list, sorted_list):
    merge_sort(unsorted_list)
    assert unsorted_list == sorted_list

def test_merge_sort_empty_list():
    empty_list = []
    merge_sort(empty_list)
    assert empty_list == []

def test_merge_sort_single_element():
    single_element_list = [5]
    merge_sort(single_element_list)
    assert single_element_list == [5]

def test_merge_sort_duplicate_elements():
    duplicate_list = [5, 3, 1, 2, 1, 4, 3, 5]
    merge_sort(duplicate_list)
    assert duplicate_list == [1, 1, 2, 3, 3, 4, 5, 5]

def test_merge_sort_reverse_sorted():
    reverse_sorted_list = [6, 5, 4, 3, 2, 1]
    merge_sort(reverse_sorted_list)
    assert reverse_sorted_list == [1, 2, 3, 4, 5, 6]

def test_merge_sort_already_sorted(sorted_list):
    merge_sort(sorted_list)
    assert sorted_list == sorted_list

def test_merge_sort_expected_failure():
    unsortable_list = [8, 'a', 23, 42, 16, 15]
    with pytest.raises(TypeError):
        merge_sort(unsortable_list)
