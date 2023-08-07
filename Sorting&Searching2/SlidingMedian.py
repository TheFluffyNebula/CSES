import sys
sys.stdin = open("Slidingmedian.in")

n, k = map(int,input().split())
a = list(map(int,input().split()))

# yeah... no
''' gpt
from heapq import *

def medianSlidingWindow(nums, k):
    def rebalance():
        while len(lowers) < len(highers):
            heappush(lowers, -heappop(highers))
        while len(lowers) > len(highers) + 1:
            heappush(highers, -heappop(lowers))

    lowers, highers = [], []
    for i in range(k):
        heappush(lowers, -nums[i])
    rebalance()

    medians = [-lowers[0] if k % 2 else (highers[0] - lowers[0]) / 2.0]
    for i in range(k, len(nums)):
        if nums[i - k] <= -lowers[0]:
            lowers.remove(-nums[i - k])
        else:
            highers.remove(nums[i - k])
        heappush(lowers, -nums[i])
        rebalance()
        medians.append(-lowers[0] if k % 2 else (highers[0] - lowers[0]) / 2.0)

    return medians

'''