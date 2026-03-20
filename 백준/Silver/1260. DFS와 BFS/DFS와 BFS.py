import sys
from collections import deque

input=sys.stdin.readline

def dfs(v):
    visited[v]=1
    print(v, end=' ')
    for i in list[v]:
        if visited[i] == 0:
            dfs(i)


def bfs(v):
    visited[v] = 1
    q=deque([v])
    while q:
        node=q.popleft()
        print(node, end=' ')
        for i in list[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


n,m,v=map(int,input().split())
list=[[] for i in range(n+1)]
visited=[0 for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    list[x].append(y)
    list[y].append(x)

for i in range(1, n+1):
    list[i].sort()

dfs(v)
print()
visited = [0 for _ in range(n+1)]
bfs(v)


