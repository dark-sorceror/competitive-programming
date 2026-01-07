# https://leetcode.com/problems/reverse-words-in-a-string/

def reverseWords(s: str) -> str:
    return " ".join(i.strip() for i in s.split()[::-1]) # (0 ms)