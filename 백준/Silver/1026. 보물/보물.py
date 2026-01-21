import sys

input = sys.stdin.readline
S=0

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(n):
    S+=a[i]*b[i]
sys.stdout.write(str(S))