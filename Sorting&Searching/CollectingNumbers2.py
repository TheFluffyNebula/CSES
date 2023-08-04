import sys
sys.stdin = open("CollectingNumbers2.in")
from collections import defaultdict
n, q = map(int,input().split())
a = list(map(int,input().split()))

order = [0] * n
for i in range(n):
    order[a[i] - 1] = i + 1
# print(order)
loc = defaultdict(int) # key=object, value = index
for i in range(n):
    # print(order[i])
    loc[order[i]] = i + 1
# print(loc)

firstDecrease = 0
for i in range(n - 1):
    if order[i + 1] < order[i]:
        firstDecrease += 1

def swap(swap1, swap2):
    # print(loc, order)
    swap1_index, swap2_index = loc[swap1] - 1, loc[swap2] - 1
    order[swap1_index], order[swap2_index] = order[swap2_index], order[swap1_index] # update ord
    loc[swap1], loc[swap2] = loc[swap2], loc[swap1] # update loc
    # print(loc, order)

decreases = [firstDecrease]
for query in range(q):
    a, b = map(int,input().split())
    a, b = min(a, b), max(a, b) # in case b > a
    assert a != b
    print(a,b)
    # count decreases before and decreases after
    # possible edges cases: a or b on edge and a adjacent to b
    # can address edge with bound checking
    # can address adjacency with set() to avoid duplicates
    decreasesBefore = set()
    if loc[a] != 0:
        if order[loc[a] - 1] > order[loc[a]]:
            decreasesBefore.add((loc[a] - 1, loc[a]))
    if loc[a] != n - 1:
        if order[loc[a]] > order[loc[a] + 1]:
            decreasesBefore.add((loc[a], loc[a] + 1))
    if loc[b] != 0:
        if order[loc[b] - 1] > order[loc[b]]:
            decreasesBefore.add((loc[b] - 1, loc[b]))
    if loc[b] != n - 1:
        if order[loc[b]] > order[loc[b] + 1]:
            decreasesBefore.add((loc[b], loc[b] + 1))
    swap(a,b)
    decreasesAfter = set()
    if loc[a] != 0:
        if order[loc[a] - 1] > order[loc[a]]:
            decreasesAfter.add((loc[a] - 1, loc[a]))
    if loc[a] != n - 1:
        if order[loc[a]] > order[loc[a] + 1]:
            decreasesAfter.add((loc[a], loc[a] + 1))
    if loc[b] != 0:
        if order[loc[b] - 1] > order[loc[b]]:
            decreasesAfter.add((loc[b] - 1, loc[b]))
    if loc[b] != n - 1:
        if order[loc[b]] > order[loc[b] + 1]:
            decreasesAfter.add((loc[b], loc[b] + 1))
    decreases.append(decreases[-1] + len(decreasesAfter) - len(decreasesBefore))
    print(order, loc)
    print(decreasesBefore, decreasesAfter)
print(decreases)
    
'''
one index card later
it appears that in the order list, you swap the numbers themselves in the order[] list
swapping is rather easy due to multi-assignment
but even then, there are still m queries which could be difficult
might have to look at what's around the swaps and what changes
okay, I think I'll just do this since it's just a few list lookups and nothing that screams o(n) per query
way too complicated way too fast :/
'''