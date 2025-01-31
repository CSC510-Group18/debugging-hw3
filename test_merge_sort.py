from hw2_debugging import merge_sort


def test_merge_sort_random():
    array = [3, 1, 2, 5, 4]
    assert merge_sort(array) == sorted(array)


def test_merge_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == arr


def test_merge_sort_empty():
    arr = []
    assert merge_sort(arr) == arr


def test_merge_sort_single():
    arr = [1]
    assert merge_sort(arr) == arr
