import sys # TLE bc python :/
# sys.stdin = open("RoomAllocation.in")
import heapq

N = int(input())
v = []

for i in range(N):
    a, b = map(int, input().split())
    v.append(((a, b), i))

v.sort()

rooms = 0
last_room = 0
ans = [0]*N
pq = []

for i in range(N):
    if not pq:
        last_room += 1
        heapq.heappush(pq, (v[i][0][1], last_room))
        ans[v[i][1]] = last_room
    else:
        minimum = pq[0]
        if minimum[0] < v[i][0][0]:
            heapq.heappop(pq)
            heapq.heappush(pq, (v[i][0][1], minimum[1]))
            ans[v[i][1]] = minimum[1]
        else:
            last_room += 1
            heapq.heappush(pq, (v[i][0][1], last_room))
            ans[v[i][1]] = last_room

    rooms = max(rooms, len(pq))

print(rooms)
print(" ".join(map(str, ans)))


'''

'''