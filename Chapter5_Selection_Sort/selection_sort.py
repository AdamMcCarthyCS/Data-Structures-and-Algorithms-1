"""
Selection Sort
Steps: 
    1) Loop over all indexes except the last in the array, this will be automatically sorted when reached
    2) Assume the lowest value is at the outer index i initially
    3) Check the indexes to the right of the outer index i for lower values than the current lowest
    4) If a lower value is found at and inner index j change the lowest value index to j
    5) After checking all inner indexes if the lowest value index has changed from i then swap
        the value at i the value at the new index
Time complexity: O(n^2)
Notes: Selection sort takes approximately half the number of steps as bubble sort
"""

def selection_sort(array: list[int]):
    for outer_index in range(len(array) - 1):
        lowest_value_index = outer_index

        for inner_index in range(outer_index + 1, len(array)):
            if array[inner_index] < array[lowest_value_index]:
                lowest_value_index = inner_index

        if lowest_value_index != outer_index:
            array[lowest_value_index], array[outer_index] = array[outer_index], array[lowest_value_index]

    return array

# Test cases:
# - empty list
# - single item
# - already sorted
# - reverse sorted
# - duplicates
def test_selection_sort_with_edge_cases():
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]
    print("All test cases passed!")
    

if __name__ == "__main__":    
    test_selection_sort_with_edge_cases() 