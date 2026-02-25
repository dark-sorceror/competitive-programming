# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

def sortByBits(arr: list[int]) -> list[int]:
    return sorted(arr, key = lambda x: (x.bit_count(), x)) # (0 ms)