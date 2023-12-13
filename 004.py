H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
A_t = [list(x) for x in zip(*A)]
a = []
a_t = []
for h in range(H):
    a.append(sum(A[h]))
for w in range(W):
    a_t.append(sum(A_t[w]))
for h in range(H):
    output = ''
    for w in range(W):
        output += str(a[h]+a_t[w]-A[h][w])+' '
    print(output)