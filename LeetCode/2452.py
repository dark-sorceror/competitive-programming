# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

def twoEditWords(queries: list[str], dictionary: list[str]) -> list[str]:
    a = []

    for i in queries:
        for j in dictionary:
            if sum(a != b for a, b in zip(i, j)) <= 2:
                a.append(i)

                break

    return a # (117 ms)