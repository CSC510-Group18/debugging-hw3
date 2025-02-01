"""
Homework 2 Debugging
"""

import random


def merge_sort(arr):
    """Sort an array using merge sort"""
    if len(arr) == 1 or len(arr) == 0:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_array, right_array):
    """Recombine two sorted arrays into a single sorted array"""
    left_index = 0
    right_index = 0
    merge_index = 0
    merge_arr = [None] * (len(left_array) + len(right_array))

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merge_arr[merge_index] = left_array[left_index]
            left_index += 1
        else:
            merge_arr[merge_index] = right_array[right_index]
            right_index += 1
        merge_index += 1

    while right_index < len(right_array):
        merge_arr[merge_index] = right_array[right_index]
        right_index += 1
        merge_index += 1

    while left_index < len(left_array):
        merge_arr[merge_index] = left_array[left_index]
        left_index += 1
        merge_index += 1

    return merge_arr


def linear_search(arr, item):
    """
    Finds the index of an item in the array and return this index.
    If not found, this function returns None
    """

    for i, value in enumerate(arr):
        if value == item:
            return i
    return None


if __name__ == "__main__":
    print("Testing...")

    sample_array = [random.randint(0, 100) for _ in range(20)]

    assert sorted(sample_array) == merge_sort(sample_array), "Merge sort is not working"

    idx = random.randint(0, len(sample_array) - 1)
    x = sample_array[idx]

    assert idx == linear_search(sample_array, x), "Linear search is not working"

    print("All tests passed!")
