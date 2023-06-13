# CC 26

## Sorting algorthim blog article

The output of processing this input array:

[8,4,23,42,16,15]

Pass 1:

we intialize the sorted array variable with the value at index 0 in our case (8) in the input array, 
we then start the iteration over the input array for (length - 1) times to compare and sort using the insert function; we send the sorted array [8] along with the second element of the input array (4), the insert fun. first check if the value (4) is greater than (8) to increase the index by 1 its not so it then checks if the array index has changed and >= the length of the sorted array meaning that its less so 
it stores the (8) on a temp var. and assert (4) as the new index (0) and (8) in its place then increase the index i by 1 so it exits the loop and the value is appended to the end of the array so the: 


[4,8]

Pass 2:

the second iteration would have [4,8] as the sorted array and (23) as the input it will also compare it with the element at index (0) which is now (4) and since it is greater than (4) it will enter the first loop and the index is increased by (1) so that we can compare it with the 2nd element (8) it is greater so it exits the first loop and the second loop cond. is false since 2 !< 2 and append 23 to the end :

[4,8,23]

Pass 3:

the 3red iteration would have [4,8,23] as the sorted array and (42) as the input it will also compare it with the element at index (0) which is now (4) and since it is greater than (4) it will enter the first loop and the index is increased by (1) so that we can compare it with the 2nd element (8) it is greater and one more time with (23) so it exits the first loop and the second loop cond. is false since 3 !< 3 and append 42 to the end :

[4,8,23,42]

Pass 4:

the 3red iteration would have [4,8,23,42] as the sorted array and (16) as the input it will also compare it with the element at index (0) which is now (4) and since it is greater than (4) it will enter the first loop and the index is increased by (1) so that we can compare it with the 2nd element (8) it is greater and one more time with (23) which is less than so it exits the first loop and the second loop cond. is true since 2 < 4 so it stores the (23) on a temp var. and assert (16) as the new index (2) and (23) in its place then increase the index i by 1 and does the same for (23,42) then it exits the loop and the value (42) is appended to the end of the array so the: 
 :

[4,8,16,23,42]

Pass 4:

the 3red iteration would have [4,8,16,23,42] as the sorted array and (15) as the input it will also compare it with the element at index (0) which is now (4) and since it is greater than (4) it will enter the first loop and the index is increased by (1) so that we can compare it with the 2nd element (8) it is greater and one more time with (16) which is less than so it exits the first loop and the second loop cond. is true since 2 < 5 so it stores the (16) on a temp var. and assert (15) as the new index (2) and (16) in its loc. then increase the index i by 1 and does the same for (16,23) and then (23,42) then it exits the loop and the value (42) is appended to the end of the array so the: 
 :

[4,8,15,16,23,42]



- The efficiency of the `InsertionSort` algorithm in terms of time complexity is as follows:

    - Best Case: If the input list is already sorted, the algorithm will make a single pass through the list to check each element, resulting in a time complexity of O(n).
    - Average Case: In the average case, the algorithm requires comparing and shifting elements for each input element, resulting in a time complexity of O(n^2).
    - Worst Case: In the worst case, when the input list is sorted in reverse order, the algorithm will make comparisons and shifts for each element, resulting in a time complexity of O(n^2).

    The efficiency of the `InsertionSort` algorithm in terms of space complexity is as follows:

    - The algorithm sorts the list in-place, meaning it modifies the input list directly. Therefore, the space complexity is O(1) as it does not require any additional space proportional to the input size.

    The efficiency of the `Insert` function in terms of time complexity is O(n) in the worst case, as it may need to shift all the elements to insert the value at the correct position. The space complexity of the `Insert` function is O(1) since it performs the insertion in-place, modifying the existing list.
