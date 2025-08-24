import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = -1  # 방문 처리

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = -1
                queue.append((nx, ny))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                bfs(x, y)
                count += 1
    print(count)
