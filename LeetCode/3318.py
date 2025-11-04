# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

def findXSum(nums: list[int], k: int, x: int) -> list[int]:
    t = []
    s = 0
    for i in range(len(nums) - k + 1):
        d = dict()

        for j in set(nums[i : i + k]):
            d[j] = nums[i : i + k].count(j)
        
        soa = dict(sorted(d.items(), key=lambda item: (item[1], item[0]), reverse=True))

        s = 0
        
        for i in range(x):
            s += list(soa.values())[i] * list(soa.keys())[i]
            
        t.append(s)
    
    return t