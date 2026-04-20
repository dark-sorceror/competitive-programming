# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/

def maxDistance(nums1: list[int], nums2: list[int]) -> int:
    i = j = r = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            r = max(r, j - i)
            j += 1
        else:
            i += 1

    return r # (59 ms)