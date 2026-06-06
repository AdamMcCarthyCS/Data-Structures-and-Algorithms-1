"""
Speeding up an O(n^2) algorithm to O(n) using a lookup table
"""


"""
An O(n^2) implementation of finding duplicates
"""
def has_duplicates_slow(array: list[int]):
    array_length = len(array)

    for i in range(array_length):
        for j in range(array_length):
            if i != j and array[i] == array[j]:
                return True
    return False

def test_has_duplicates_slow():
    assert has_duplicates_slow([1, 2, 3, 4, 5]) == False
    assert has_duplicates_slow([1, 2, 3, 4, 5, 1]) == True
    print("All tests passed!")

def has_duplicates_fast(array: list[int]):
    checker_list = [0] * 11

    for value in array:
        if checker_list[value] == 1:
            return True
        else: 
            checker_list[value] = 1
    return False

def test_has_duplicates_fast():
    assert has_duplicates_fast([1, 2, 3, 4, 5]) == False
    assert has_duplicates_fast([1, 2, 3, 4, 5, 1]) == True
    print("All tests passed!")

"""
An O(n) implementation of finding the largest value in an array
"""
def greatest_number(array: list[int]):
    if len(array) == 0:
        return None
    else:
        greatest_number = array[0]
        for index in range(1, len(array)):
            if array[index] > greatest_number:
                greatest_number = array[index]
        return greatest_number

def test_greatest_number():
    assert greatest_number([]) == None
    assert greatest_number([1]) == 1
    assert greatest_number([1, 2, 3, 4, 5]) == 5
    assert greatest_number([5, 4, 3, 2, 1]) == 5
    print("All tests passed!")

if __name__ == "__main__":
    test_has_duplicates_slow()
    test_has_duplicates_fast()
    test_greatest_number()