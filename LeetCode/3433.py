# https://leetcode.com/problems/count-mentions-per-user/

from collections import defaultdict

def countMentions(numberOfUsers: int, events: list[list[str]]) -> list[int]:
    m = [0] * numberOfUsers
    us = defaultdict(int)

    tmp = {"OFFLINE": 0, "MESSAGE": 1}

    se = [] # Timestamp, event type key, event
    for i in events:
        t = int(i[1])
        et = i[0]
        tk = tmp[et]

        se.append((t, tk, i))
    
    se.sort()

    for i, j, k in se:
        et = k[0]

        for uid in range(numberOfUsers):
            if us[uid] > 0 and i >= us[uid]: 
                us[uid] = 0
        
        if et == "OFFLINE":
            uid = int(k[2])
            us[uid] = i + 60
        elif et == "MESSAGE":
            ms = k[2]
            mids = []
            
            if ms == "ALL":
                mids = list(range(numberOfUsers))
            else:
                tok = ms.split()

                for n in tok:
                    if n.startswith("id") and n[2:].isdigit():
                        uid = int(n[2:])

                        if 0 <= uid < numberOfUsers:
                            mids.append(uid)

            for n in mids:
                if us[uid] == 0:
                    m[uid] += 1
                    
    return m