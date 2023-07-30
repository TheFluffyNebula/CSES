import sys
# sys.stdin = open("NumberSpiral.in")
for _ in range(int(input())):
    a, b = map(int,input().split())
    level = max(a,b)
    if level % 2 == 0: #even
        if a == level: #subtract from mx
            ans = level**2 - (b - 1)
        else:
            ans = (level - 1)**2 + 1 + (a - 1)
    else:
        if a == level:
            ans = (level - 1)**2 + 1 + (b - 1)
        else:
            ans = level**2 - (a - 1)
    print(ans)

'''
mx number determines what level the coordinate is on
ex. (1,1) -> 1
(2,1) or (1, 2) or (2,2) -> 2
level goes up to mx^2 

lv 2: mx^2 is (2,1) while (mx-1)^2 + 1 is (1,2)
lv 3: mx^2 is (1,3) while (mx-1)^2 + 1 is (3,1)
lv 4: mx^2 is (4,1)
lv 5: mx^2 is (1,5)
'''