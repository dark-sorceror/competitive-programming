# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

import heapq

def minimumPairRemoval(nums: list[int]) -> int:
    n = len(nums)

    l = list(range(-1, n - 1))
    r = list(range(1, n + 1))

    c, o = 0, 0

    pq = []

    def is_inverted(i, j):
        if i == -1 or j == n: return False

        return nums[i] > nums[j]

    for i in range(n - 1):
        s = nums[i] + nums[i + 1]
        heapq.heappush(pq, (s, i))

        if nums[i] > nums[i + 1]: c += 1
    
    while c > 0:
        v = False

        while pq:
            s, i = heapq.heappop(pq)
            j = r[i]
            
            if j < n and l[j] == i and (nums[i] + nums[j] == s):
                v = True

                break
        
        if not v: break
        
        if is_inverted(l[i], i): c -= 1
        if is_inverted(i, j): c -= 1

        k = r[j]

        if is_inverted(j, k): c -= 1

        nums[i] = nums[i] + nums[j]

        r[i] = k

        if k < n: l[k] = i
        if is_inverted(l[i], i): c += 1
        if is_inverted(i, k): c += 1
        if l[i] != -1:
            heapq.heappush(pq, (nums[l[i]] + nums[i], l[i]))

        if k < n:
            heapq.heappush(pq, (nums[i] + nums[k], i))
        
        o += 1
        
    return o # (2195 ms)