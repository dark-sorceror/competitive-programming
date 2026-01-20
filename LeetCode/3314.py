# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

def minBitwiseArray(nums: list[int]) -> list[int]:
    ans = []

    for i in nums:
        for j in range(1, 10):
            if (i >> j) & 1 == 0:
                ans.append(i ^ (1 << (j - 1)))

                break
    
    return ans