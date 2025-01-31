from hw2_debugging import merge_sort


def test_merge_sort_random():
    assert merge_sort([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]


def test_merge_sort_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_single():
    assert merge_sort([1]) == [1]
