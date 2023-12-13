N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()
for q in range(Q):
    B = int(input())
    left = 0
    right = N-1
    if B <= A[left]:
        print(A[left]-B)
        continue
    if B >= A[right]:
        print(B-A[right])
        continue
    bingo = False
    while right - left > 1:
        mid = (right+left)//2
        if B == A[mid]:
            print(0)
            bingo = True
            break
        if B < A[mid]:
            right = mid
        if B > A[mid]:
            left = mid
    if bingo == False:
        print(min(B-A[left], A[right]-B))