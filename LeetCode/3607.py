# https://leetcode.com/problems/power-grid-maintenance/

def processQueries(c: int, connections: list[list[int, int]], queries: list[list[int, int]]) -> list[int]:
    g, o = [] if not connections else [i for i, j in connections.append([0, len(connections) + 1])], []

    for i, j in queries:
        if not g: return [1, -1]
            
        if i == 1:
            if j in g: o.append(j)
            else: o.append(g[0])
        else: g.remove(j)

    return o