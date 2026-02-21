# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

def countPrimeSetBits(left: int, right: int) -> int:
    p = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
    a = 0

    for i in range(left, right + 1):
        if i.bit_count() in p:
            a += 1

    return a # (22 ms)