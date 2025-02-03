"""
BogoSort Implementation
Citation: https://www.geeksforgeeks.org/python-program-for-bogosort-or-permutation-sort/
"""
import random


def bogo_sort(a):
    """
    Main method for BogoSort implementation
    """
    while is_sorted(a) is False:
        shuffle(a)

def is_sorted(a):
    """
    Checks if input array is sorted or not

    Inputs: a --> input array

    Outputs: True if array is sorted, False otherwise
    """
    n = len(a)
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return False
    return True

def shuffle(a):
    """
    Generates a permutation of the array

    Inputs: a --> input array
    """
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]
