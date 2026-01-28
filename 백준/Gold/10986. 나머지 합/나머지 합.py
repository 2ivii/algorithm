import sys

input=sys.stdin.readline

n,m=map(int,input().split())

arr = list(map(int,input().split()))
S=[0]*(n+1)
M=[0]*(n+1)
cnt=0

for i in range(1,n+1):
    S[i] = S[i-1] + arr[i-1]

for i in range(1,n+1):
    M[i] = S[i]%m
    if M[i] == 0:
        cnt+=1

count=[0] * m
for x in M[1:]:
    count[x]+=1

for i in range(m):
    cnt+=count[i]*(count[i]-1)//2

print(cnt)



