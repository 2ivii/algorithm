N=int(input())
arr=[]
s=0
for _ in range(N):
    x=int(input())
    arr.append(x)

arr.sort()

for i in range(N):
    s+=abs(i+1-arr[i])

print(s)