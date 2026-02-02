# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

import heapq
from collections import defaultdict

def minimumCost(nums: list[int], k: int, dist: int) -> int:
    t = k - 1
        
    a = nums[1:]
    n = len(a)
    
    max_h = [] 
    min_h = []

    l_max = defaultdict(int)
    l_min = defaultdict(int)
    
    c = 0
    max_h_n = 0
    
    def clean_max_h():
        while max_h and l_max[-max_h[0]] > 0:
            l_max[-heapq.heappop(max_h)] -= 1
    
    def clean_min_h():
        while min_h and l_min[min_h[0]] > 0:
            l_min[heapq.heappop(min_h)] -= 1

    l = min(dist + 1, n)

    for i in range(l):
        v = a[i]
        c += v
        max_h_n += 1

        heapq.heappush(max_h, -v)

    while max_h_n > t:
        v = -heapq.heappop(max_h)
        c -= v
        max_h_n -= 1

        heapq.heappush(min_h, v)
        
    m = c
    
    # Sliding Window
    for i in range(1, n - dist):
        out_ = a[i - 1]
        in_ = a[i + dist]

        clean_max_h()

        is_in_small = False

        if max_h and out_ <= -max_h[0]:
            is_in_small = True
        
        if is_in_small:
            c -= out_
            max_h_n -= 1
            l_max[out_] += 1
        else:
            l_min[out_] += 1

        clean_max_h()

        if max_h and in_ < -max_h[0]:
            c += in_
            max_h_n += 1

            heapq.heappush(max_h, -in_)
        else:
            heapq.heappush(min_h, in_)

        while max_h_n < t:
            clean_min_h()

            if min_h:
                v = heapq.heappop(min_h)
                c += v
                max_h_n += 1

                heapq.heappush(max_h, -v)

        while max_h_n > t:
            clean_max_h()

            if max_h:
                v = -heapq.heappop(max_h)
                c -= v
                max_h_n -= 1

                heapq.heappush(min_h, v)
        
        m = min(m, c)
        
    return m + nums[0] # (357 ms)