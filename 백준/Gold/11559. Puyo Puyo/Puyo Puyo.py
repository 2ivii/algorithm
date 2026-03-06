import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(field, visited, x, y):
    color = field[x][y]
    q = deque([(x, y)])
    visited[x][y] = True
    group = [(x, y)]

    while q:
        v, w = q.popleft()
        for i in range(4):
            sx, sy = v + dx[i], w + dy[i]
            if 0 <= sx < 12 and 0 <= sy < 6:
                if not visited[sx][sy] and field[sx][sy] == color:
                    visited[sx][sy] = True
                    q.append((sx, sy))
                    group.append((sx, sy))

    return group


def pang(field, targets):
    for x, y in targets:
        field[x][y] = '.'


def fall(field):
    for j in range(6):
        temp = []
        for i in range(11, -1, -1):
            if field[i][j] != '.':
                temp.append(field[i][j])

        for i in range(11, -1, -1):
            if temp:
                field[i][j] = temp.pop(0)
            else:
                field[i][j] = '.'


field = [list(input().strip()) for _ in range(12)]

answer = 0

while True:
    visited = [[False] * 6 for _ in range(12)]
    boom = []

    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                group = bfs(field, visited, i, j)
                if len(group) >= 4:
                    boom.extend(group)

    if not boom:
        break

    pang(field, boom)
    fall(field)
    answer += 1

print(answer)