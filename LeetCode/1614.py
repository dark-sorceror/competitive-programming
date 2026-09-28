# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2026-09-28

def maxDepth(self, s: str) -> int:
	co = 0
        cc = 0
        diff = 0

        for i in s:
            if i == "(":
                co += 1
            elif i == ")":
                cc += 1

            diff = max(diff, co - cc)

        return diff # (0 ms)
