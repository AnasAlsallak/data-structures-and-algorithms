from typing import List

def merge_sort(arr: List[int]) -> None:
    """
    Sorts the given list in ascending order using the Merge Sort algorithm.

    Args:
        arr (List[int]): The list to be sorted.
    """

    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        # Sort the left side
        merge_sort(left)
        # Sort the right side
        merge_sort(right)

        # Merge the sorted left and right sides together
        merge(left, right, arr)


def merge(left: List[int], right: List[int], arr: List[int]) -> None:
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (List[int]): The left subarray.
        right (List[int]): The right subarray.
        arr (List[int]): The array to store the merged result.
    """

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy any remaining elements from the left subarray
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right subarray
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
