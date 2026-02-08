import sys

input = sys.stdin.readline

S,P = map(int,input().split())

arr=list(input().strip())

check = list(map(int,input().split()))
my = [0]*4
cnt=0

def myadd(c):
    if c == 'A':
        my[0]+=1
    elif c == 'C':
        my[1]+=1
    elif c == 'G':
        my[2]+=1
    elif c == 'T':
        my[3]+=1

def myremove(c):
    if c == 'A':
        my[0] -= 1
    elif c == 'C':
        my[1] -= 1
    elif c == 'G':
        my[2] -= 1
    elif c == 'T':
        my[3] -= 1


for i in range(P):
    myadd(arr[i])

if my[0]>=check[0] and my[1]>=check[1] and my[2]>=check[2] and my[3]>=check[3]:
    cnt+=1

for i in range(P,S):
    myadd(arr[i])
    myremove(arr[i-P])
    if my[0]>=check[0] and my[1]>=check[1] and my[2]>=check[2] and my[3]>=check[3]:
        cnt+=1

print(cnt)
