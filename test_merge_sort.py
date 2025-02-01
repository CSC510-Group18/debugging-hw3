"""
Modle tests merge_sort function
"""
from hw2_debugging import merge_sort


def test_merge_sort_random():
    """Test merge_sort with a randomly ordered array."""
    array = [3, 1, 2, 5, 4]
    assert merge_sort(array) == sorted(array)


def test_merge_sort_sorted():
    """Test merge_sort with an already sorted array."""
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == arr


def test_merge_sort_empty():
    """Test merge_sort with an empty array."""
    arr = []
    assert merge_sort(arr) == arr


def test_merge_sort_single():
    """Test merge_sort with a single-element array."""
    arr = [1]
    assert merge_sort(arr) == arr
