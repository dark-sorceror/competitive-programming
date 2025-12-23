# https://leetcode.com/problems/two-best-non-overlapping-events/

import heapq 

def maxTwoEvents(events: list[list[int]]) -> int:
    events.sort(key=lambda x: x[0])

    m_h = []
    m_v, a = 0, 0
    
    for s, e, v in events:
        while m_h and m_h[0][0] < s:
            n_v = heapq.heappop(m_h)[1]
            m_v = max(m_v, n_v)

        a = max(a, v + m_v)

        heapq.heappush(m_h, (e, v))
        
    return a # (155 ms)