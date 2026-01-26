import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
S=[0]
for i in range(1,n+1):
    S.append(S[i-1]+arr[i-1])

for _ in range(m):
    x,y=map(int,input().split())
    print(S[y]-S[x-1])
