N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def judge(M:int):
    global N, L, K, A
    count = 0
    a = 0
    for n in range(N):
        if A[n]-a >= M:
            a = A[n]
            count += 1
    if L-a >= M:
        count += 1
    if count >= K+1:
        return True
    return False

left = 0
right = L
while right-left > 1:
    mid = (left+right)//2
    if judge(mid) == False:
        right = mid
    else:
        left = mid
print((left+right)//2)