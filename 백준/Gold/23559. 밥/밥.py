N,X=map(int,input().split())
arr=[]
s=0
for _ in range(N):
    x=list(map(int,input().split()))
    arr.append(x)

arr.sort(key=lambda x:abs(x[1]-x[0]), reverse=True)

X-=N*1000 # 돈을 탕진하는걸 방지하기 위해 하루에 최소 천원씩은 무조건 써야되므로 미리 빼두기

for i in range(N):
    if arr[i][0] < arr[i][1]:
        s+=arr[i][1]
    elif X>=4000:
        s+=arr[i][0]
        X-=4000
    else:
        s+=arr[i][1]

print(s)
