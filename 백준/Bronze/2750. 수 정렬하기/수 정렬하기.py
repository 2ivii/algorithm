import sys

input = sys.stdin.readline

n=int(input())
arr=[int(input()) for _ in range(n)]

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp

for i in range(n):
    print(arr[i])