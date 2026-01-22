import sys

input=sys.stdin.readline

n=int(input())
numbers=list(input().strip())
s=0

for i in numbers:
    s+=int(i)

sys.stdout.write(str(s))