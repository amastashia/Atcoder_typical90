N = int(input())
S = input()

atcoder = 'atcoder'
M = len(atcoder)
dp = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N+1)]
dp[0][0] = 1
for n in range(N):
    for m in range(M):
        dp[n+1][m] += dp[n][m]
        if S[n] == atcoder[m]:
            dp[n+1][m+1]+=dp[n][m]
    dp[n+1][M] += dp[n][M]
    for m in range(M+1): 
        dp[n+1][m] %= 1e9+7

print(int(dp[N][7]))