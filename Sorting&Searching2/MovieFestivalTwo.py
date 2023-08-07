import sys
# sys.stdin = open("MovieFestivalTwo.in")

n, k = map(int,input().split())
# n movies, k people
friends = [0] * k
times = [tuple(map(int,input().split())) for _ in range(n)]
times.sort(key = lambda x: x[1])
# print(friends, times)

friendNum = 0
ans = 0
for i in range(n):
    if friends[friendNum] <= times[i][0]:
        ans += 1
        friends[friendNum] = times[i][1]
    friendNum += 1
    if friendNum == k:
        friendNum = 0
print(ans)

'''
attempt 1: maintain the most recent times and then always catch the earliest ending films
this will probably end up being n*k time which is likely too slow
although... I do have a feeling that there is a chance
There's a chance I can always iterate through linearly through the friends list
since the ending times **are** sorted, so the friends list may be sorted correctly always
    it got close
attempt 2:
"However, if a friend has to finish watching a movie before they can start watching another, 
you need to ensure that the movies assigned to a particular friend don't overlap.
In that case, you'd need a priority queue or a heap to keep track of when each friend is free to watch a new movie. 
You would pop the friend who is free the soonest, check if they can watch the next movie,
and if so, update their free time and push them back into the heap. If they can't, you would move on to the next movie."
'''