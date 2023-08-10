import sys
# sys.stdin = open("StaticMinQueries.in")
input = sys.stdin.readline
import math

MAX_N = int(3e5)
LOG = 20

a = [0]*MAX_N
m = [[0]*LOG for _ in range(MAX_N)]

def query(L, R): 
    length = R - L + 1
    k = int(math.log2(length))
    return min(m[L][k], m[R-(2**k)+1][k])

# 1) read input
n, q = map(int,input().split())
a = list(map(int,input().split()))

for i in range(n):
    m[i][0] = a[i]

# 2) preprocessing, O(N*log(N))
for k in range(1, LOG):
    for i in range(n - (2**k) + 1):  # changed loop condition here
        m[i][k] = min(m[i][k-1], m[i+(2**(k-1))][k-1])

# 3) answer queries
for i in range(q):
    L, R = map(int, input().split())
    print(query(L - 1, R - 1))

'''
errichto vid: https://www.youtube.com/watch?v=0jWeUdxrGm4
'''