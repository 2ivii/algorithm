N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_value = 0
for i in range(0,N):
    for j in range (i+1,N):
        for k in range(j+1,N):
            if max_value < arr[i] + arr[j] + arr[k] and arr[i] + arr[j] + arr[k] <= M:
                max_value = arr[i] + arr[j] + arr[k]
print(max_value)