import sys
sys.stdin = open("DiceCombinations.in")
input = sys.stdin.readline
import functools

n = int(input())
@functools.cache
def dice(x):
    if x < 0:
        return 0
    return dice(x - 1) + dice(x - 2) + dice(x - 3) + dice(x - 4) + dice(x - 5) + dice(x - 6)
print(dice(n))
'''
n = 3 example: 
0: 0
1: 1
2: 2
3: 3
'''