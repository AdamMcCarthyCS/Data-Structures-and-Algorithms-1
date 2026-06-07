"""
Binary Search
- Requires an ordered array to perform
- Time complexity: O(log n)
- Drops approx half the search space in each step
- Middle value chosen to be middle (odd length), left of two middle values (even length)
"""

def binary_search(sorted_array: list[int], value: int):
    lower_bound = 0
    upper_bound = len(sorted_array) - 1
    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        value_at_midpoint = sorted_array[midpoint]
        if value_at_midpoint == value:
            return midpoint
        elif value_at_midpoint > value:
            upper_bound = midpoint - 1
        else: 
            lower_bound = midpoint + 1

    return None


# =====================================================================
# =====================================================================

# This function will test the binary search function with a large array and various values, including edge cases.
def test_binary_search():
    large_array = list(range(-5000, 5001))
    assert binary_search(large_array, 0) == 5000
    assert binary_search(large_array, -5000) == 0
    assert binary_search(large_array, 5000) == 10000
    assert binary_search(large_array, -5001) == None
    assert binary_search(large_array, 5001) == None  
    assert binary_search(large_array, 1234) == 6234 
    assert binary_search(large_array, -1234) == 3766
    assert binary_search(large_array, 999) == 5999
    assert binary_search(large_array, -999) == 4001     

# This function will test the binary search function with edge cases, such as an empty array and an array with only one element.
def test_edge_cases():
    array = []
    assert binary_search(array, 1) == None
    array = [1]
    assert binary_search(array, 1) == 0
    assert binary_search(array, 0) == None
    assert binary_search(array, 2) == None  

# This function will return the number of steps taken to find a value in a sorted array using binary search.
def binary_search_step_count(sorted_array: list[int], value: int):
    count = 0
    lower_bound = 0
    upper_bound = len(sorted_array) - 1
    while lower_bound <= upper_bound:
        count += 1
        midpoint = (lower_bound + upper_bound) // 2
        value_at_midpoint = sorted_array[midpoint]
        if value_at_midpoint == value:
            return count
        elif value_at_midpoint > value:
            upper_bound = midpoint - 1
        else: 
            lower_bound = midpoint + 1

    return count

# This function will print the number of steps taken to find various values in a large array using binary search.
def print_binary_search_step_count():
    large_array = list(range(-50000, 50001))
    print("Steps to find 0:", binary_search_step_count(large_array, 0))
    print("Steps to find -5000:", binary_search_step_count(large_array, -5000))
    print("Steps to find 5000:", binary_search_step_count(large_array, 5000))
    print("Steps to find -5001:", binary_search_step_count(large_array, -5001))
    print("Steps to find 5001:", binary_search_step_count(large_array, 5001))  
    print("Steps to find 1234:", binary_search_step_count(large_array, 1234)) 
    print("Steps to find -1234:", binary_search_step_count(large_array, -1234))
    print("Steps to find 999:", binary_search_step_count(large_array, 999))
    print("Steps to find -999:", binary_search_step_count(large_array, -999))   

if __name__ == "__main__":
    test_binary_search()
    test_edge_cases()
    print_binary_search_step_count()
    print("All tests passed!")