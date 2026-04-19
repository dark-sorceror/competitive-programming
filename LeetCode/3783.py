# https://leetcode.com/problems/mirror-distance-of-an-integer/

def mirrorDistance(n: int) -> int:
    return abs(n - int(str(n)[::-1])) # (0 ms)