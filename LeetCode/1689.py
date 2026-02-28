# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

def minPartitions(n: str) -> int:
    return int(max(n)) # (9 ms)