import sys
# sys.stdin = open("Repetitions.in")
s = input()
mxRep = 0
curRep = 0
for i in range(len(s) - 1):
    if s[i + 1] == s[i]:
        curRep += 1
    else:
        mxRep = max(mxRep, curRep)
        curRep = 0
mxRep = max(mxRep, curRep)
print(mxRep + 1)