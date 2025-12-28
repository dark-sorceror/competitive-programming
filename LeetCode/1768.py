# https://leetcode.com/problems/merge-strings-alternately/

def mergeAlternately(word1: str, word2: str) -> str:
    m = "".join(i + j for i, j in [*zip(word1, word2)])

    if len(word1) > len(word2):
        m += word1[len(word2):]
    elif len(word2) > len(word1):
        m += word2[len(word1):]
    
    return m # (29 ms)