import sys

input=sys.stdin.readline

arr=list(input().strip())
l=len(arr)

for i in range(l):
    m=i
    for j in range(i,l):
        if arr[m]<arr[j]:
            m=j
    temp=arr[m]
    arr[m]=arr[i]
    arr[i]=temp
    
for i in range(l):
    print(arr[i],end='')