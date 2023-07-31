import sys # LOL IT WORKS :DDD
# sys.stdin = open("AppleDivision.in")
n = int(input())
nums = list(map(int,input().split()))
tot = sum(nums)

#code from GrayCode2.py
a = [0]
def generate(nums, val):
    b = nums.copy()
    b.append(val)
    b.extend(nums)
    return b
for i in range(1, n):
    a = generate(a, i)
# print(a, len(a))

first = 0
best = 1e10
states = [False] * n # whether they're in the sum or not
# print(states)
for i in range(2**n - 1):
    if states[a[i]]: # if in the sum then subtract
        first -= nums[a[i]]
    else: # if not in the sum then add
        first += nums[a[i]]
    states[a[i]] = not states[a[i]]
    second = tot - first
    best = min(best, abs(first - second))
    # print(first)
print(best)

