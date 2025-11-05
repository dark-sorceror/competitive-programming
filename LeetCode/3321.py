# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii

def findXSum(nums: list[int], k: int, x: int) -> list[int]:
    t = []

    for i in range(len(nums) - k + 1):
        d = dict()

        for j in nums[i : i + k]:
            d[j] = d.get(j, 0) + 1
        
        sd = sorted(d.items(), key=lambda item: (-item[1], -item[0]))

        s = 0

        if len(sd) < x: s = sum(nums[i : i + k])
        else:
            for j in range(x):
                s += sd[j][0] * sd[j][1]
            
        t.append(s)
    
    return t