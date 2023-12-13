import sys
sys.setrecursionlimit(1000000)

N=int(input())
adj = {}
for i in range(N-1):
    a, b = map(int, input().split())
    if not a in adj:
        adj[a] = {b}
    else:
        adj[a].add(b)

    if not b in adj:
        adj[b] = {a}
    else:
        adj[b].add(a)

u = 0
max_len = 0
def dfs(adj, v, visited = None, len = 0):
    global u, max_len
    if visited == None:
        visited = set()
    visited.add(v)
    if max_len < len:
        max_len = len
        u = v
    for next_v in adj[v]-visited:
        dfs(adj, next_v, visited, len+1)
    return u, max_len

s, _ = dfs(adj, 1)
_, result = dfs(adj, s)
print(result+1)