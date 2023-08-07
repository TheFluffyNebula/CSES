import sys
sys.stdin = open("SumOfFourValues.in")

n, target = map(int,input().split())
b = list(map(int,input().split()))
a = [(b[i], i + 1) for i in range(n)]
a.sort()
# print(a)
# split array into two halves
a1 = a[:n//2] # splitPoint = n // 2
a2 = a[n//2:]
print(a1, a2)
# calc all possible pair sums for each list
sum_a1 = []
for i in range(len(a1)):
    for j in range(i + 1, len(a1)):
        if i != j:
            sum_a1.append((a1[i][0] + a1[j][0], a1[i][1], a1[j][1]))
sum_a1.sort()
sum_a2 = []
for i in range(len(a2)):
    for j in range(i + 1, len(a2)):
        if i != j:
            sum_a2.append((a2[i][0] + a2[j][0], a2[i][1], a2[j][1]))
sum_a2.sort()
sum_a1.extend(sum_a2)
print(sum_a1)
# at this point I realize there might be overlap so I ask gpt to finish it
# headed to SoFV2.py now

'''
looking up the solution
according to chatgpt:
Split the array into two halves.
Calculate all possible sums of two elements for each half and store them in two lists.
Sort both lists.
For each element in the first list, find a pair in the second list such that the sum of the pair is equal to the target. 
This can be done in O(n) time using the Two Pointers technique, because the lists are sorted.
'''