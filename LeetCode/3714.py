# https://leetcode.com/problems/longest-balanced-substring-ii/

def longestBalanced(s: str) -> int:
    n = len(s)

    if n == 0:
        return 0
    
    max_len = 0
    
    current_run = 0

    for i in range(n):
        if i > 0 and s[i] == s[i-1]:
            current_run += 1
        else:
            current_run = 1
        max_len = max(max_len, current_run)
        
    pairs = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    
    for char1, char2 in pairs:
        mp = {0: -1}
        balance = 0
        
        for i, char in enumerate(s):
            if char == char1:
                balance += 1
            elif char == char2:
                balance -= 1
            else:
                mp = {0: i}
                balance = 0

                continue
            
            if balance in mp:
                max_len = max(max_len, i - mp[balance])
            else:
                mp[balance] = i
    
    mp = {(0, 0): -1}
    counts = {'a': 0, 'b': 0, 'c': 0}
    
    for i, char in enumerate(s):
        counts[char] += 1
        
        diff_ab = counts['a'] - counts['b']
        diff_bc = counts['b'] - counts['c']
        state = (diff_ab, diff_bc)
        
        if state in mp:
            max_len = max(max_len, i - mp[state])
        else:
            mp[state] = i
            
    return max_len # (884 ms)