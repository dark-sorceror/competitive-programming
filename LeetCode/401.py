# https://leetcode.com/problems/binary-watch/?envType=daily-question&envId=2026-02-17

def readBinaryWatch(turnedOn: int) -> list[str]:
    r = []

    for h in range(12):
        for m in range(60):
            if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                r.append(f"{h}:{m:02d}")
                
    return r # (0 ms)