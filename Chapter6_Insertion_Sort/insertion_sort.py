"""
Insertion Sort
Steps:
- Loop over all the array indexes starting from the second position
    - Store the value of the array which corresponds to the initial index of the loop
    - Set a variable to hold the (position) index of the variable immediately left of the loop initial index
    - Start an inner loop which continues while the position index is greater than or equal to zero
        - If the value at each position is larger than the stored value move it one position to the right and move the position index left
        - Otherwise if a value smaller than or equal to the stored value is encountered break out of the inner loop
    - Insert the stored value back into the space to the right of the position index
Average Case: ~ n^2 / 2 steps
Worst Case: ~ n^2 steps  
Big O: O(n^2)
"""

def insertion_sort(array: list[int]):
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1

        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                position -= 1
            else:
                break
        array[position + 1] = temp_value

    return array

# test empty array
# test single element array
# test already sorted array
# test reverse sorted array
# test array with duplicate values
def test_insertion_sort():
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([3, 1, 2, 3]) == [1, 2, 3, 3]
    print("All tests passed!")

if __name__ == "__main__":
    test_insertion_sort()