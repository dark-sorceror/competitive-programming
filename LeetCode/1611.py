# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

def minimumOneBitOperations(n: int) -> int:
    r = 0

    while n:
        r ^= n
        n >>= 1

    return r # (0 ms)