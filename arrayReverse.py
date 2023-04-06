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

    print("All test cases pass")

test_reverse_array()
