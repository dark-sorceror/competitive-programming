# https://leetcode.com/problems/special-binary-string/

def makeLargestSpecial(self, s: str) -> str:
    c, i, a = 0, 0, []

    for j, char in enumerate(s):
        c += 1 if char == '1' else -1
        
        if c == 0:
            a.append('1' + self.makeLargestSpecial(s[i + 1 : j]) + '0')
            i = j + 1

    a.sort(reverse = True)

    return "".join(a) # (0 ms)