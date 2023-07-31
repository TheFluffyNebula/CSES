import sys # nope, doesn't work for n >= 4
sys.stdin = open("GrayCode.in")

n = int(input())
chars = [0] * n
cur = 0
up = True
ans = []
for i in range(2**n):
    ans.append("".join(map(str,chars)))
    chars[cur] = 1 - chars[cur]
    if cur == 0 and up == False:
        cur = 1
        up = True
    elif cur == n - 1 and up == True:
        cur = n - 2
        up = False
    else:
        if up == True:
            cur += 1
        else:
            cur -= 1

print(*ans, sep = "\n")

'''
working out an example on paper gives
0-1-0
0-1-2-1-0-1-2
which means the next is probably
0-1-2-3-2-1-0-1-2-3...
'''