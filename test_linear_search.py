
from hw2_debugging import linear_search


def test_linear_search_found():
    array = [1, 2, 3, 4, 5]
    assert linear_search(array, 3) == 2


def test_linear_search_not_found():
    array = [1, 2, 3, 4, 5]
    assert linear_search(array, 6) is None


def test_linear_search_empty():
    array = []
    assert linear_search(array, 1) is None
