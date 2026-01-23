import sys

input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

M=max(arr)
print(100/M*sum(arr)/n)