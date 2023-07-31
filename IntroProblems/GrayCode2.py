import sys #works :)
# sys.stdin = open("GrayCode.in")

n = int(input())

a = [0]
def generate(nums, val):
    b = nums.copy()
    b.append(val)
    b.extend(nums)
    return b

for i in range(1, n):
    a = generate(a, i)
# print(a)

chars = [0] * n
ans = ["".join(map(str, chars))]
for i in range(2**n - 1):
    chars[a[i]] = 1 - chars[a[i]]
    ans.append("".join(map(str,chars)))
    
print(*ans, sep = "\n")


'''
attempt 2
for the 4-sequence it seems to be
0-1-0-2-0-1-0-2-0-1-0-3-0-1-0-2-0-1-0
for the 3 sequence it could be
0-1-0-2-0-1-0
oh I see it now, it's a recursion of sorts
0 -> (0), 1, (0)
(0, 1, 0) -> (0, 1, 0), 2, (0, 1, 0)
(0, 1, 0, 2, 0, 1, 0) -> (0, 1, 0, 2, 0, 1, 0), 3, (0, 1, 0, 2, 0, 1, 0)
'''