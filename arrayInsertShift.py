def insertShiftArray(arr, val):
    """
    Inserts the passed value at the middle integer index of the passed array.
    
    Parameters:
    arr : The input array.
    val: The value we want to add.
    
    Returns:
    o_arr: The output array with the new value added at the middle integer index.
    """
    l = len(arr)
    if l == 0:
        return [val]
    elif l == 1:
        if val < arr[0]:
            return [val, arr[0]]
        else:
            return [arr[0], val]
    elif l % 2 == 0:
        mid = l // 2
    else:
        mid = (l + 1) // 2

    o_arr = []
    for i in range(l):
        if i == mid:
            o_arr.append(val)
        o_arr.append(arr[i])
        
    return o_arr


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

    print("All test cases pass")

test_insertShiftArray()


