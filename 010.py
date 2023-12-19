N = int(input())
P_class1, P_class2 = [], []
sum1, sum2 = 0, 0
for n in range(N):
    c, p = list(map(int, input().split()))
    if c == 1:
        sum1 += p
    else:
        sum2 += p
    P_class1.append(sum1)
    P_class2.append(sum2)

Q = int(input())
for _ in range(Q):
    l, r = list(map(int, input().split()))
    if l == 1:
        A = P_class1[r-1]
        B = P_class2[r-1]
    else:
        A = P_class1[r-1]-P_class1[l-2]
        B = P_class2[r-1]-P_class2[l-2]
    print(A, B)
