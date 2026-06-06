"""
Linear ordered search
- Searches ordered ordered_arrays
- Time Complexity: O(n)
- Finishes early if it finds a value larger than search value
- Takes N steps for N valued ordered_array if search value is not in ordered_array
"""

def linear_ordered_search(ordered_array: list[int], search_value: int):
    ordered_array_length = len(ordered_array)
    for index in range(ordered_array_length):
        if ordered_array[index] == search_value:
            return index
        if ordered_array[index] > search_value:
            break
    return -1

def test_linear_ordered_search():
    ordered_array = [1, 2, 3, 4, 5]
    assert linear_ordered_search(ordered_array, 3) == 2
    assert linear_ordered_search(ordered_array, 6) == -1
    assert linear_ordered_search(ordered_array, 0) == -1
    assert linear_ordered_search(ordered_array, 1) == 0
    assert linear_ordered_search(ordered_array, 5) == 4

def test_edge_cases():
    ordered_array = []
    assert linear_ordered_search(ordered_array, 1) == -1
    ordered_array = [1]
    assert linear_ordered_search(ordered_array, 1) == 0
    assert linear_ordered_search(ordered_array, 0) == -1
    assert linear_ordered_search(ordered_array, 2) == -1

if __name__ == "__main__":
    test_linear_ordered_search()
    test_edge_cases()
    print("All tests passed!")