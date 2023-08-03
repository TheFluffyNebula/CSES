import sys
# sys.stdin = open("MovieFestival.in")
input = sys.stdin.readline

# classic greedy problem, take the one that ends the earliest
n = int(input())
times = [tuple(map(int,input().split())) for _ in range(n)]
times.sort(key = lambda x: x[1])
# print(times)

# dont need this
# maxTime = max(element for sublist in times for element in sublist)
# print(maxTime)

curTime = 0
ans = 0
for L in range(n):
    if curTime <= times[L][0]:
        ans += 1
        curTime = times[L][1]
print(ans)

# pointer approach