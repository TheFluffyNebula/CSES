import sys
sys.stdin = open("DynamicSumQueries.in")
input = sys.stdin.readline

n, q = map(int,input().split())
a = list(map(int,input().spilt()))
for _ in range(q):
    a, b = map(int,input().split())