N, K = map(int, input().split())
S = input()

arr = [[N for _ in range(26)] for _ in range(N)]
for i in reversed(range(N)):
    arr[i][ord(S[i])-ord('a')] = i
    if i == 0:
        break
    for j in range(26):
        arr[i-1][j] = arr[i][j]

output = ''
current = 0
for k in range(K):
    for alphabets in range(26):
        next = arr[current][alphabets]
        if N-next+k >= K:
            output += chr(ord('a')+ alphabets)
            current = next+1
            break
print(output)