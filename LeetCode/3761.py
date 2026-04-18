# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

def minMirrorPairDistance(nums: list[int]) -> int:
    def reverse_int(x: int) -> int:
        return int(str(x)[::-1])

    h = {}
    m = float('inf')

    for i, j in enumerate(nums):
        if j in h:
            m = min(m, i - h[j])

        h[reverse_int(j)] = i
        
    return m if m != float('inf') else -1 # (218 ms)