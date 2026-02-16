class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.min_val = [0] * (4 * size)
        self.max_val = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push(self, node):
        if self.lazy[node] != 0:
            lz = self.lazy[node]
       
            self.lazy[2 * node] += lz
            self.min_val[2 * node] += lz
            self.max_val[2 * node] += lz
           
            self.lazy[2 * node + 1] += lz
            self.min_val[2 * node + 1] += lz
            self.max_val[2 * node + 1] += lz

            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if r < start or end < l:
            return

        if l <= start and end <= r:
            self.lazy[node] += val
            self.min_val[node] += val
            self.max_val[node] += val
            
            return

        self._push(node)
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        
        self.min_val[node] = min(self.min_val[2 * node], self.min_val[2 * node + 1])
        self.max_val[node] = max(self.max_val[2 * node], self.max_val[2 * node + 1])

    def find_first_zero(self, node, start, end):
        if self.min_val[node] > 0 or self.max_val[node] < 0:
            return -1
        
        if start == end:
            return start if self.min_val[node] == 0 else -1
        
        self._push(node)
        mid = (start + end) // 2

        res = self.find_first_zero(2 * node, start, mid)

        if res != -1:
            return res
            
        return self.find_first_zero(2 * node + 1, mid + 1, end)


def longestBalanced(nums: list[int]) -> int:
    n = len(nums)
    st = SegmentTree(n)
    last_pos = {}
    m = 0
    
    for r, num in enumerate(nums):
        prev = last_pos.get(num, -1)

        val = 1 if num % 2 == 0 else -1
        st.update(1, 0, n - 1, prev + 1, r, val)
        
        last_pos[num] = r

        l = st.find_first_zero(1, 0, n - 1)
        
        if l != -1:
            if l <= r:
                m = max(m, r - l + 1)
                
    return m # (7510 ms)