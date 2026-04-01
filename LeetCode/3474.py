# https://leetcode.com/problems/lexicographically-smallest-generated-string/

def generateString(str1: str, str2: str) -> str:
    n, m = len(str1), len(str2)
    L = n + m - 1
    word = ['?'] * L

    for i in range(n):
        if str1[i] == 'T':
            for j in range(m):
                if word[i + j] != '?' and word[i + j] != str2[j]:
                    return ""

                word[i + j] = str2[j]

    for i in range(L):
        if word[i] == '?':
            word[i] = 'a'

    for i in range(n):
        if str1[i] == 'F':
            if "".join(word[i : i + m]) == str2:
                fixed = False

                for j in range(m - 1, -1, -1):
                    is_forced = False
                    
                    for k in range(max(0, i + j - m + 1), min(n, i + j + 1)):
                        if str1[k] == 'T':
                            is_forced = True

                            break
                    
                    if not is_forced:
                        word[i + j] = 'b' 
                        fixed = True

                        break
                
                if not fixed: return ""

    return "".join(word) # (139 ms)