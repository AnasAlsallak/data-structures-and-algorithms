def reverse_array(arr):
    """
    Reverses the order of elements in an array.

    Parameters:
        arr : The array to be reversed.

    Returns:
        arr: The reversed array.
    """
    arr_len = len(arr)
    # Loop through the first half of the array and swap elements
    i = 0
    while i < arr_len // 2:
        # Calculate the index of the corresponding element from the end of the array
        j = arr_len - 1 - i
        # Swap the elements using a temporary variable
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1

    return arr


