import sys
# sys.stdin = open("TwoSets.in")
import bisect
n = int(input())
triangle = n * (n + 1) / 2
if triangle % 2 == 1:
    print("NO")
else:
    cur = 0
    halfway = triangle // 2
    rem = halfway
    ans = []
    for i in range(n, n // 2, -1):
        if rem - i < 1:
            continue
        cur += i
        ans.append(i)
        rem -= i
        if rem <= n / 2:
            ans.append(int(rem))
            break
    ans.reverse()
    ans2 = []
    for i in range(1, n + 1):
        a, b = bisect.bisect_left(ans, i), bisect.bisect(ans, i)
        if a == b:
            ans2.append(i)
    print("YES")
    print(len(ans))
    print(*ans)
    print(len(ans2))
    print(*ans2)

'''
1: sum=1    no
2: sum=3    no
3: sum=6    yes, (1, 2) and (3)
4: sum=10   yes, (1, 4) and (2, 3)
5: sum=15   no
6: sum=21   no
7: sum=28   yes, (1, 6, 7) and (2, 3, 4, 5)
8: sum=36   yes, (8, 7, 3)
check if triangle number is even
if no, print no
if yes, add highest stuff until you're really close
'''