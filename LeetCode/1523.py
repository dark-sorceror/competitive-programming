# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

def countOdds(low: int, high: int) -> int:
    return (high + 1) // 2 - low // 2 # (8 ms)