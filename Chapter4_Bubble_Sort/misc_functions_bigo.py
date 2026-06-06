"An O(n) prime number checker"
def is_prime(number: int):
    for value in range(2, number):
        if number % value == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(14) == False
    assert is_prime(15) == False    
    print("All tests passed!")

"An O(1) leap year checker"
def is_leap_year(year: int):
    if year % 100 == 0 and year % 400 != 0:
        return False
    return year % 4 == 0

def test_is_leap_year():
    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2004) == True
    assert is_leap_year(2001) == False
    print("All tests passed!")

"A O(log n) solver for the number of chess board squares needed for n grains of rice"
def count_spaces_for_n_grains(grains: int):
    chessboard_spaces = 1
    number_of_grains = 1
    while number_of_grains < grains:
        number_of_grains *= 2
        chessboard_spaces += 1
    return chessboard_spaces

def test_count_spaces_for_n_grains():
    assert count_spaces_for_n_grains(1) == 1
    assert count_spaces_for_n_grains(2) == 2
    assert count_spaces_for_n_grains(3) == 3
    assert count_spaces_for_n_grains(4) == 3
    assert count_spaces_for_n_grains(5) == 4
    assert count_spaces_for_n_grains(8) == 4
    assert count_spaces_for_n_grains(9) == 5
    assert count_spaces_for_n_grains(15) == 5
    assert count_spaces_for_n_grains(16) == 5
    assert count_spaces_for_n_grains(17) == 6
    print("All tests passed!")

"""An O(1) implementation of finding the median of a sorted array"""
def find_median_sorted(sorted_array: list[int]):
    array_length = len(sorted_array)
    middle_index = array_length // 2

    if array_length == 0:
        return None
    elif array_length == 1:
        return sorted_array[0]
    # if array length is even
    elif array_length % 2 == 0:
        return (sorted_array[middle_index - 1] + sorted_array[middle_index]) / 2
    # if array length is odd
    return sorted_array[middle_index]

def test_find_median_sorted():
    assert find_median_sorted([]) == None
    assert find_median_sorted([1]) == 1
    assert find_median_sorted([1, 2]) == 1.5
    assert find_median_sorted([1, 2, 3]) == 2
    assert find_median_sorted([1, 2, 3, 4]) == 2.5
    assert find_median_sorted([1, 2, 3, 4, 5]) == 3
    print("All tests passed!")
    


if __name__ == "__main__":
    test_is_prime()
    test_is_leap_year()
    test_count_spaces_for_n_grains()
    test_find_median_sorted()
    