'''
Test binary search functionality
'''

from binary_search import binary_search


def test_binary_search_found():
    """Test binary_search when the target is found in the array."""
    array = [1, 2, 3, 4, 5]
    assert binary_search(array, 3) == 2


def test_binary_search_not_found():
    """Test binary_search when the target is not found in the array."""
    array = [1, 2, 3, 4, 5]
    assert binary_search(array, 6) is None


def test_binary_search_empty():
    """Test binary_search with an empty array."""
    array = []
    assert binary_search(array, 1) is None
