class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.sums = [0] * (2 * self.size)

    def build_segment(self, a: list, x, lx, rx):
        if (rx - lx == 1):
            if (lx < len(a)):
                self.sums[x] = a[lx]
            return
        m = (lx + rx) // 2
        self.build_segment(a, 2 * x + 1, lx, m)
        self.build_segment(a, 2 * x + 2, m, rx)
        self.sums[x] = self.sums[2 * x + 1] + self.sums[2 * x + 2]

    def build_all(self, a: list):
        self.build_segment(a, 0, 0, self.size)

    def set_segment(self, i, v, x, lx, rx): # set values for the segment tree
        if rx - lx == 1: # bottom level, set the value
            self.sums[x] = v
            return;
        m = (lx + rx) // 2
        if i < m:
            self.set_segment(i, v, 2 * x + 1, lx, m)
        else:
            self.set_segment(i, v, 2 * x + 2, m, rx)
        self.sums[x] = self.sums[2 * x + 1] + self.sums[2 * x + 2]

    def set_all(self, i, v): # set index to value
        self.set_segment(i, v, 0, 0, self.size)

    def sum_segment(self, l, r, x, lx, rx):
        if lx >= r or l >= rx:
            return 0
        if lx >= l and rx <= r:
            return self.sums[x]
        m = (lx + rx) // 2
        s1 = self.sum_segment(l, r, 2 * x + 1, lx, m)
        s2 = self.sum_segment(l, r, 2 * x + 2, m, rx)
        return s1 + s2
    
    def sum_all(self, l, r):
        return self.sum_segment(l, r, 0, 0, self.size)