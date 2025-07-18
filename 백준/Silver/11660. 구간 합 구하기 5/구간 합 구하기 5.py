n,m=map(int,input().split())
arr=[]
prefix = [[0 for i in range(0, n + 1)] for _ in range(n + 1)]
for i in range(n):
    x=list(map(int,input().split()))
    arr.append(x)


for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i - 1][j - 1]

for _ in range(m):
    i, j, x, y = map(int, input().split())
    answer = prefix[x][y] - prefix[x][j - 1] - prefix[i - 1][y] + prefix[i - 1][j - 1]
    print(answer)
