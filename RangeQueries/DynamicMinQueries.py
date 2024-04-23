# Segment Tree for the Minimum
# tried print optimization, still TLE
# need cpp unfortunately
import sys
# sys.stdin = open("DynamicMinQueries.in")
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.mins = [0] * (2 * self.size)

    def build_segment(self, a: list, x, lx, rx):
        if (rx - lx == 1):
            if (lx < len(a)):
                self.mins[x] = a[lx]
            return
        m = (lx + rx) // 2
        self.build_segment(a, 2 * x + 1, lx, m)
        self.build_segment(a, 2 * x + 2, m, rx)
        self.mins[x] = min(self.mins[2 * x + 1], self.mins[2 * x + 2])

    def build_all(self, a: list):
        self.build_segment(a, 0, 0, self.size)

    def set_segment(self, i, v, x, lx, rx): # set values for the segment tree
        if rx - lx == 1: # bottom level, set the value
            self.mins[x] = v
            return;
        m = (lx + rx) // 2
        if i < m:
            self.set_segment(i, v, 2 * x + 1, lx, m)
        else:
            self.set_segment(i, v, 2 * x + 2, m, rx)
        self.mins[x] = min(self.mins[2 * x + 1], self.mins[2 * x + 2])

    def set_all(self, i, v): # set index to value
        self.set_segment(i, v, 0, 0, self.size)

    def min_segment(self, l, r, x, lx, rx):
        if lx >= r or l >= rx:
            return float('inf')
        if lx >= l and rx <= r:
            return self.mins[x]
        m = (lx + rx) // 2
        s1 = self.min_segment(l, r, 2 * x + 1, lx, m)
        s2 = self.min_segment(l, r, 2 * x + 2, m, rx)
        return min(s1, s2)
    
    def min_all(self, l, r):
        return self.min_segment(l, r, 0, 0, self.size)
    
n, m = map(int,input().split())
a = list(map(int,input().split()))
st = SegmentTree(n)
st.build_all(a) # build in linear time instead of n log n
# for i in range(n):
#     st.set_all(i, a[i]) # initialize the segment tree
ans = []
for query in range(m):
    a, b, c = map(int,input().split())
    b = b - 1
    if a == 1:
        st.set_all(b, c) # set index to value
    else:
        ans.append(st.min_all(b, c))
        # print(st.min_all(b, c))
print(*ans, sep = "\n")