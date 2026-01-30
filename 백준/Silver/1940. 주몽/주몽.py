import sys

input=sys.stdin.readline

n=int(input())
m=int(input())
arr=list(map(int,input().split()))
arr.sort()

start=0
end=n-1
cnt=0
while start<end:
    if arr[start]+arr[end] < m:
        start+=1
    elif arr[start]+arr[end] == m:
        cnt+=1
        start+=1
    elif arr[start]+arr[end] > m:
        end-=1
sys.stdout.write(str(cnt))
