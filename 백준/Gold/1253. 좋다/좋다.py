import sys

input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
cnt=0
arr.sort()

for i in range(n):
    start=0
    end=n-1
    while start<end:
        if arr[start]+arr[end] == arr[i]:
            if start!=i and end!=i:
                cnt+=1
                # print(start,"번이랑",end,"번이랑",arr[start],arr[end],"의 합으로.. ",arr[i],"의 cnt는",cnt,"번")
                break
            elif start==i:
                start+=1
            else:
                end-=1
        elif arr[start]+arr[end] < arr[i]:
            start+=1
        elif arr[start]+arr[end] > arr[i]:
            end-=1
print(cnt)