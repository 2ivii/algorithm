N = int(input())
arr = []

for _ in range(N):
    x,y = map(int, input().split())
    arr.append((x,y))

for i in range(N):
    count = 0
    for j in range(N):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                count += 1
    print(count + 1, end=' ')