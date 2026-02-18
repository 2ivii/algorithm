import sys

input=sys.stdin.readline

N=int(input())
arr=[int(input().strip()) for _ in range(N)]
cnt=1
stack=[]
answer=[]

for x in arr:
    if cnt<x:
        while cnt<=x:
            stack.append(cnt)
            answer.append('+')
            cnt+=1
    elif cnt==x:
        stack.append(cnt)
        answer.append('+')
        cnt+=1
    if stack[-1]==x:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        exit(0)

for x in answer:
    print(x)


