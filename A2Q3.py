import sys

def solve(candi, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for price in candi:
        for i in range(target, price - 1, -1):
            dp[i] += dp[i - price]
    
    return dp[target]

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    if s[0] != '[' or s[-2] != ']':
        print('format error')
        exit(1)
    print(solve([int(i) for i in s[1:-2]], int(s[-1])))
