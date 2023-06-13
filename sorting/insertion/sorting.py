from typing import List

def Insert(sorted: List[int], value: int) -> None:
    """
    Inserts a value into a sorted list in the appropriate position.

    Args:
        sorted (List[int]): The sorted list.
        value (int): The value to be inserted.

    Returns:
        None. The sorted list is modified in-place.
    """
    i = 0
    length = len(sorted)
    while i < length and value > sorted[i]:
        i = i + 1
    i = min(i,length)
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i = i + 1
    sorted.append(value)


def InsertionSort(input: List[int]) -> List[int]:
    """
    Sorts a list using the insertion sort algorithm.

    Args:
        input (List[int]): The list to be sorted.

    Returns:
        List[int]: The sorted list.
    """
    sorted = [input[0]]
    for i in range(1, len(input)):
        Insert(sorted, input[i])
    return sorted
