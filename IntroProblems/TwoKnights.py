import sys
# sys.stdin = open("Twoknights.in")
n = int(input())

generate = [4 * x**2 + 12*x + 8 for x in range(n)]
# print(generate)

for i in range(1, n + 1):
    total_options = i**2 * (i**2 - 1) // 2
    if i >= 3:
        subtract = generate[i - 3]
        print(total_options - subtract)
    else:
        print(total_options)

'''
n^2 squares
n^2 * (n^2 - 1) // 2total options
subtract off all pairs of knight squares
'''