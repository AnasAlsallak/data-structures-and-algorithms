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




