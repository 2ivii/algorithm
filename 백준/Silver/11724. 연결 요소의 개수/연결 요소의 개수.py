import sys

input=sys.stdin.readline
n,m=map(int,input().split())
list=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
cnt=0

for _ in range(m):
    u,v=map(int,input().split())
    list[u].append(v)
    list[v].append(u)

def dfs(v):
    visited[v]=1
    for i in list[v]:
        if visited[i] == 0:
            dfs(i)
for i in range(1,n+1):
    if visited[i] == 0:
        cnt+=1
        dfs(i)

print(cnt)
