"""The testing module for algorithms"""


import pytest
from recursive_implementation import factorial
from binary_search import binary_search
from quick_sort import quick_sort, q_split
import random


# Tests for recursive_implementation


@pytest.mark.parametrize("number, fact", [
    (0, 1), (1, 1), (12, 479001600)
])
def test_factorial(number, fact):
    """Tests factorial_implementation function with parametrize"""
    assert factorial(number) == fact


def test_raises_value_error():
    """Tests if factorial function raises error
    in case of negative number
    """
    with pytest.raises(ValueError):
        factorial(-8)


def test_raises_type_error():
    """Tests if factorial function raises error
    in case of str argument"""
    with pytest.raises(TypeError):
        factorial('nice')

# Tests for binary_search

#
# sequence_to_test = [random.randint(1, 10) for _ in range(5)]
# print(sorted(sequence_to_test))


@pytest.mark.parametrize("sequence, search, expected", [
    ([20, 22, 31, 32, 66, 78, 85, 87, 88, 95], 66, 4), ([30, 41, 48, 67, 79, 82], 79, 4),
    ([9, 18, 19], 19, 2), ([15, 30, 46, 88], 99, None)
])
def test_binary_search(sequence, search, expected):
    """Tests binary_search algorithm uses parametrize"""
    assert binary_search(sequence, search) == expected

# Tests for quick_sort


@pytest.mark.parametrize("sequence, expected", [
    ([120, 22, 81, 32, 16, 78, 35, 7, 88, 95], [7, 16, 22, 32, 35, 78, 81, 88, 95, 120]),
    ([39, 41, 13, 111, 78, 55, 91, 2], [2, 13, 39, 41, 55, 78, 91, 111])
])
def test_quick_sort(sequence, expected):
    """Tests quick_sort algorithm uses parametrize"""
    assert quick_sort(sequence) == expected


def test_q_split():
    """Tests q_split (a part of quick_sort) function"""
    q_split([12, 99, 4, 52, 3, 8, 65, 9])
    assert [4, 3, 8, 9], [12, 99, 52, 65]


