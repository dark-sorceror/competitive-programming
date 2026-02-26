# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

def numSteps(self, s: str) -> int:
    n, c = 0, 0
    
    for i in range(len(s) - 1, 0, -1):
        if int(s[i]) + c == 1:
            n += 2
            c = 1
        else:
            n += 1

            if int(s[i]) + c == 2:
                c = 1
            else:
                c = 0
                
    return n + c # (0 ms)