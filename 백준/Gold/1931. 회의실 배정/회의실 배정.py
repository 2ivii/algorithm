N=int(input())
arr=[]
count=0
for _ in range(N):
    X=list(map(int,input().split()))
    arr.append(X)

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])
time=arr[0][0]
for i in range(N):
    if time <= arr[i][0]:
        count+=1
        time = arr[i][1]

print(count)
