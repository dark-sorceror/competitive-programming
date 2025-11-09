# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    seen, start, r = set(), 0, 0

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[start])
            start += 1
        
        seen.add(s[i])
        
        r = max(r, i - start + 1)
        
    return r # (19 ms)