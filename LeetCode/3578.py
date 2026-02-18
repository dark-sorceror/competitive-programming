# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

from collections import deque

def countPartitions(nums: list[int], k: int) -> int:
    n = len(nums)

    vp = [0] * (n + 1)
    vp[0] = 1

    p_dp = [0] * (n + 2)
    p_dp[1] = 1

    max_q = deque()
    min_q = deque()
    
    l = 0
    
    for i in range(n):
        while max_q and nums[max_q[-1]] <= nums[i]:
            max_q.pop()

        max_q.append(i)

        while min_q and nums[min_q[-1]] >= nums[i]:
            min_q.pop()

        min_q.append(i)

        while nums[max_q[0]] - nums[min_q[0]] > k:
            l += 1

            if max_q[0] < l:
                max_q.popleft()

            if min_q[0] < l:
                min_q.popleft()
        
        c = (p_dp[i + 1] - p_dp[l]) % (10**9 + 7)
        vp[i + 1] = c

        p_dp[i + 2] = (p_dp[i + 1] + c) % (10**9 + 7)
        
    return vp[n] # (498 ms)