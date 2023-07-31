import sys

n = int(input())
powers_of_5 = [5**i for i in range(1, 20)]
ans = 0
for i in range(19):
    ans += n // powers_of_5[i]
print(ans)
'''
classic math problem
find the number of factors of five
'''