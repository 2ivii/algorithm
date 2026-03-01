import sys

input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    arr.append((int(input()),i))

arr.sort()
m=0

for i in range(n):
    if m<arr[i][1]-i:
        m=arr[i][1]-i

print(m+1)


