import sys
# sys.stdin = open("CollectingNumbers.in")

n = int(input())
a = list(map(int,input().split()))
order = [0] * n
for i in range(n):
    order[a[i] - 1] = i + 1
# print(order)

decrease = 0
for i in range(n - 1):
    if order[i + 1] < order[i]:
        decrease += 1
print(decrease + 1)

'''
since the example is 4 2 1 5 3, 
I'm gonna go out on a limb and guess that it's the number of times it decreases from one element to the next
but that would mean that 1-2-3-4-5 would need zero sweeps so that can't be right
let me try listing the indexes in order then...
3 2 5 1 4
I mean, it decreases twice for a total of 1 + 2 = 3
and it also works for 12345 since that would stay 12345
let's try it!
oh wow, it worked :D
'''