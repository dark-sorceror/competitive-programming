# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

def checkOnesSegment(self, s: str) -> bool:
    return '01' not in s # (0 ms)