import sys

input=sys.stdin.readline

arr=list(input().strip())
arr.sort(reverse=True)

for i in range(len(arr)):
    print(arr[i],end='')