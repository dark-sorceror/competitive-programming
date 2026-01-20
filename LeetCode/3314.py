# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

def minBitwiseArray(nums: list[int]) -> list[int]:
    ans = []

    for i in nums:
        if i == 2: ans.append(-1)
        else:
            for j in range(1, 10):
                if (i >> j) & 1 == 0:
                    ans.append(i ^ (1 << (j - 1)))

                    break
    
    return ans # (0 ms)