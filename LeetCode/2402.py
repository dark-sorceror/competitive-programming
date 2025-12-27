# https://leetcode.com/problems/meeting-rooms-iii/

import heapq

def mostBooked(n: int, meetings: list[list[int]]) -> int:
    meetings.sort()
    
    f_r = list(range(n))
    heapq.heapify(f_r)

    b_r = []

    c = [0] * n
    
    for s, e in meetings:
        while b_r and b_r[0][0] <= s:
            r = heapq.heappop(b_r)[1]
            heapq.heappush(f_r, r)

        if f_r:
            r = heapq.heappop(f_r)
            heapq.heappush(b_r, (e, r))
        else:
            c_e, r = heapq.heappop(b_r)

            n_e = c_e + (e - s)
            heapq.heappush(b_r, (n_e, r))

        c[r] += 1

    return c.index(max(c)) # (163 ms)