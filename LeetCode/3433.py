# https://leetcode.com/problems/count-mentions-per-user/

import heapq

def countMentions(numberOfUsers: int, events: list[list[str]]) -> list[int]:
    m, on, off = [0] * numberOfUsers, [True] * numberOfUsers, []
    ac = 0
    tmp = {"OFFLINE": 0, "MESSAGE": 1}
    se = sorted(events, key=lambda e: (int(e[1]), tmp[e[0]]))

    for i in se:
        et, t, c = i
        t = int(t)
        
        while off and off[0][0] <= t:
            i, j = heapq.heappop(off)
            on[j] = True
        
        if et == "OFFLINE":
            uid = int(c)
            on[uid] = False
            
            heapq.heappush(off, (t + 60, uid))
        elif et == "MESSAGE":
            if c == "ALL": ac += 1
            elif c == "HERE":
                for k in range(numberOfUsers):
                    if on[k]: m[k] += 1
            else:
                tok = c.split()

                for n in tok:
                    if n.startswith("id") and n[2:].isdigit():
                        uid = int(n[2:])

                        if 0 <= uid < numberOfUsers: m[uid] += 1

    for i in range(numberOfUsers):
        m[i] += ac
                    
    return m