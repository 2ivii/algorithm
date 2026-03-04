import sys
from collections import deque

input=sys.stdin.readline

w,h=map(int,input().split())

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

def bfs(i,j,w,h,m):
    queue=deque([(i,j)])
    m[i][j] = 0
    while queue:
        x,y = queue.popleft()
        for k in range(8):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0 <= nx < h and 0 <= ny < w and m[nx][ny] == 1 :
                m[nx][ny] = 0
                queue.append((nx,ny))


while w != 0 and h != 0:
    m=[list(map(int,input().split())) for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                bfs(i,j,w,h,m)
                cnt+=1
    print(cnt)
    w, h = map(int, input().split())

