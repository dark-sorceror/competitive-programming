# https://leetcode.com/problems/reverse-vowels-of-a-string/

def reverseVowels(s: str) -> str:
    s, v = list(s), ['a', 'e', 'i', 'o', 'u']
    l, r = 0, len(s) - 1

    while l < r:
        if s[l].lower() not in v:
            l += 1

            continue

        if s[r].lower() not in v:
            r -= 1

            continue

        s[l], s[r] = s[r], s[l]

        l += 1
        r -= 1
    
    return "".join(s) # (15 ms)