"""
Bubble Sort
- Time Complexity: O(n^2)
- Each iteration moves the largest remaining array element to the correct position
- For array of size n the worst case scenario is:
    - n passes through the array
    - n + (n - 1) + .. + 1 comparisons
- As it's O(n^2) its impractical for larger arrays
- An array of 100 elements ~10000 algorithm steps
"""

def bubble_sort(some_list: list[int]):
    sorted_until = len(some_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for index in range(sorted_until):
            if some_list[index] > some_list[index + 1]:
                some_list[index], some_list[index + 1] = some_list[index + 1], some_list[index]
                sorted = False
        sorted_until -= 1
    return some_list
        

def test_bubble_sort():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    print("All tests passed!")



if __name__ == "__main__":
    test_bubble_sort()
    