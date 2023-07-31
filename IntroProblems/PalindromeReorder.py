import sys
# sys.stdin = open("PalindromeReorder.in")
from collections import defaultdict, deque
s = input()
nums = defaultdict(int)
for character in s:
    nums[character] += 1
# print(nums)
oddNums = 0
single = ""
for x in nums.keys():
    if nums[x] % 2 == 1:
        single = x
        oddNums += 1

if oddNums > 1:
    print("NO SOLUTION")
else:
    d = deque(single)
    nums[single] -= 1
    for x in nums.keys():
        for i in range(nums[x] // 2):
            d.appendleft(x)
            d.append(x)
    print("".join(d))