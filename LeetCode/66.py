# https://leetcode.com/problems/plus-one/

def plusOne(digits: list[int]) -> list[int]:
    return [int(i) for i in str(int("".join(str(i) for i in digits)) + 1)] # (0 ms)