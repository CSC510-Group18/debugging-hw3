"""
BogoSort Implementation
Citation: https://www.geeksforgeeks.org/python-program-for-bogosort-or-permutation-sort/
"""
import random

"""
Main method for BogoSort implementation
"""
def bogo_sort(a):
    n = len(a)
    while is_sorted(a)== False:
        shuffle(a)

"""
Checks if input array is sorted or not

Inputs: a --> input array

Outputs: True if array is sorted, False otherwise
"""
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return False
    return True

"""
Generates a permutation of the array

Inputs: a --> input array
"""

def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]
