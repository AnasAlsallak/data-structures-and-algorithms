def binary_search(arr, target):
    """
    Search for a target value in a sorted array using binary search algorithm.

    Args:
        arr (list): A sorted list of integers.
        target (int): The integer value to search for in the list.

    Returns:
        int: The index of the target value in the input array if found, otherwise -1.

    """
    # Initialize left and right pointers to the beginning and end of the array
    left = 0
    right = len(arr) - 1

    # Continue searching while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the midpoint of the search interval
        mid = (left + right) // 2

        # If the midpoint is the target value, return its index
        if arr[mid] == target:
            return mid
        # If the midpoint is less than the target, move the left pointer to the right of the midpoint
        elif arr[mid] < target:
            left = mid + 1
        # If the midpoint is greater than the target, move the right pointer to the left of the midpoint
        else:
            right = mid - 1

    # If the target value is not found, return -1
    return -1
