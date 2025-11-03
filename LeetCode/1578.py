# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

def minCost(colors: str, neededTime: list[int]) -> int:
    colors = list(colors)
    
    g, gl = 0, []
    
    for i in range(len(colors)):
        if len(gl) == 0: gl.append([colors[i]])
        else:
            if colors[i] == gl[g][0]: gl[g].append(colors[i])
            else:
                gl.append([colors[i]])
                g += 1
    
    s, ix = 0, 0   
    
    for i in range(len(gl)):
        for j in range(len(gl[i])):
            gl[i][j] = neededTime[ix]
            ix += 1
        
        s += sum(gl[i]) - max(gl[i])

    return s # (338 ms)