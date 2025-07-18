n,m = map(int,input().split())

arr = list(map(int, input().split()))
prefix = [0]

for i in range(n):
    prefix.append(prefix[i]+arr[i])

for i in range(m):
    start,end = map(int,input().split())
    print(prefix[end]-prefix[start-1])
    