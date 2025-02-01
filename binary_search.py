"""Module provides a binary search function"""

def binary_search(haystack, needle):
    """Function implements binary search on a sorted array."""
    # https://stackoverflow.com/questions/3755136/pythonic-way-to-check-if-a-list-is-sorted-or-not
    assert all(haystack[i] <= haystack[i+1] for i in range(len(haystack) - 1))
    left = 0
    right = len(haystack) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if haystack[mid] == needle:
            return mid
        if haystack[mid] < needle:
            left = mid + 1

        right = mid - 1

    return None
