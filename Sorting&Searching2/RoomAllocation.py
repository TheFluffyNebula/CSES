import sys
sys.stdin = open("RoomAllocation.in")

n = int(input())
vals = []
for i in range(n):
    a, b = map(int,input().split())
    vals.append((a, b))
vals.sort(key=lambda x: (x[1], -x[0]))
print(vals)

def check(rMax):
    rooms = [0] * rMax  # departure time of last visitor in each room

    for arrival, departure in vals:
        for i in range(rMax):
            if arrival > rooms[i]:  # visitor can be accommodated in room i
                rooms[i] = departure
                break
        else:  # no break, i.e., visitor couldn't be accommodated in any room
            return False

    return True

L = 1
R = int(2e5)
ans = 0
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
    # print(mid, check(mid))
print(ans)

'''
first theory: 
constantly find the earliest next booking
second theory:
binary search on how many rooms are required
[0,0,1,1] find the first 1
but then there's still the issue of who actually gets which room
third theory:
standard interval approach, coordinate compression into the paint problem
'''