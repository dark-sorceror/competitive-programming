class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        x_s = set()
        
        for x, y, l in squares:
            x_s.add(x)
            x_s.add(x + l)

        x_s = sorted(list(x_s))
        m = {val: i for i, val in enumerate(x_s)}
        
        n = len(x_s) - 1
        c = [0] * n
        s = [] # (y, t, x_s, x_e)
        
        for x, y, l in squares:
            s.append((y, 1, x, x + l))
            s.append((y + l, -1, x, x + l))
            
        s.sort(key = lambda e: e[0])

        t = 0.0
        strips = [] # (y_b, y_t, w, a)
        
        # Sweep
        for i in range(len(s) - 1):
            y, t, x1, x2 = s[i]

            l = m[x1]
            r = m[x2]
            
            for j in range(l, r):
                c[j] += t

            n_y = s[i + 1][0]
            h = n_y - y
            
            if h > 0:
                w = 0.0
                
                for j in range(n):
                    if c[j] > 0: 
                        w += (x_s[j + 1] - x_s[j])
                
                a = w * h
                t += a
                strips.append((y, n_y, w, a))

        t_a = t / 2.0
        c_a = 0.0
        
        for y_b, y_t, w, a in strips:
            if c_a + a >= t_a:
                return y_b + (t_a - c_a) / w
            
            c_a += a
            
        return 0.0
    