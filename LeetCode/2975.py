# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

def maximizeSquareArea(m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
    def get_all_gaps(f, b):
        l = sorted(f + [1, b])
        g = set()

        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                g.add(l[j] - l[i])

        return g

    h_g = get_all_gaps(hFences, m)
    v_g = get_all_gaps(vFences, n)

    c = h_g.intersection(v_g)

    if not c: return -1

    return (max(c) ** 2) % (10**9 + 7) # (1385 ms)