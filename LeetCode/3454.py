# https://leetcode.com/problems/separate-squares-ii/

class SegmentTree:
    def __init__(self, x_c):
        self.x_c = x_c
        self.n = len(x_c) - 1
        self.c = [0] * (4 * self.n)
        self.t_l = [0.0] * (4 * self.n)

    def update(self, n, s, e, l, r, val):
        if l <= s and e <= r:
            self.c[n] += val
        else:
            m = (s + e) // 2
            l_c = 2 * n
            r_c = 2 * n + 1
            
            if l < m:
                self.update(l_c, s, m, l, r, val)
            if r > m:
                self.update(r_c, m, e, l, r, val)

        if self.c[n] > 0:
            self.t_l[n] = self.x_c[e] - self.x_c[s]
        else:
            if s + 1 == e:
                self.t_l[n] = 0.0
            else:
                self.t_l[n] = self.t_l[2 * n] + self.t_l[2 * n + 1]

def separateSquares(squares: list[list[int]]) -> float:
    x_s = set()
    
    for x, y, l in squares:
        x_s.add(x)
        x_s.add(x + l)

    x_s = sorted(list(x_s))
    st = SegmentTree(x_s)
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
        y, tp, x1, x2 = s[i]

        l = m[x1]
        r = m[x2]

        # Update segment tree
        st.update(1, 0, len(x_s) - 1, l, r, tp)

        n_y = s[i + 1][0]
        h = n_y - y
        
        if h > 0:   
            # Get total active width from the root of the tree
            w = st.t_l[1]
            a = w * h
            t += a
            strips.append((y, n_y, w, a))

    t_a = t / 2.0
    c_a = 0.0
    
    for y_b, y_t, w, a in strips:
        if (c_a + a) >= t_a:
            return y_b + (t_a - c_a) / w
        
        c_a += a
        
    return 0.0 # (2119 ms)