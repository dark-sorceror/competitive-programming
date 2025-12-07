# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

def countOdds(low: int, high: int) -> int:
    return ((high - low) + 1) // 2 if low % 2 == 0 else ((high - low) + 1) // 2 + 1