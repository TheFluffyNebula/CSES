import sys
# sys.stdin = open("CoinPiles.in")
for _ in range(int(input())):
    a, b = map(int,input().split())
    if a > 2 * b or b > 2 * a:
        print("NO")
    else:
        print("YES") if (a + b) % 3 == 0 else print("NO")