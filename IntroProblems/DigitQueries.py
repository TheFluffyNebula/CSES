import sys # this was really sloppy and was only solved after dealing with one specific edge case
# sys.stdin = open("DigitQueries.in")

for _ in range(int(input())):
    k = int(input())
    find_digit_num = [9 * 10**i for i in range(20)]
    start = [10**i for i in range(20)] #1, 10, 100, etc.
    # print(find_digit_num)
    tot = 0
    num_of_digits = 0
    for i in range(20):
        tot += find_digit_num[i] * (i + 1) # 9*1, 90*2, 900*3, etc.
        if tot > k:
            tot -= find_digit_num[i] * (i + 1)
            num_of_digits = i + 1
            break
    remaining = k - tot
    goPastStart = (remaining - 1) // num_of_digits
    currentNumber = start[num_of_digits - 1] + goPastStart
    finalRemaining = remaining - goPastStart * num_of_digits
    # print("rem", remaining)
    # print(currentNumber, finalRemaining, "num digits", num_of_digits)
    if finalRemaining > len(str(currentNumber)):
        print(9)
    else:
        print(str(currentNumber)[finalRemaining - 1])

'''
ah, the classic math problem
'''