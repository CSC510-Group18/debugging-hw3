"""
Test linear search function
"""
from hw2_debugging import linear_search


def test_linear_search_found():
    """Test linear_search when the target is found in the array."""
    array = [1, 2, 3, 4, 5]
    assert linear_search(array, 3) == 2


def test_linear_search_not_found():
    """Test linear_search when the target is not found in the array."""
    array = [1, 2, 3, 4, 5]
    assert linear_search(array, 6) is None


def test_linear_search_empty():
    """Test linear_search with an empty array."""
    array = []
    assert linear_search(array, 1) is None
