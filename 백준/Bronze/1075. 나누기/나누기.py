import sys

input = sys.stdin.readline

N = int(input().strip())
F = int(input().strip())

base = (N // 100) * 100

answer = 0
for i in range(100):
    if (base + i) % F == 0:
        answer = i
        break

print(f"{answer:02d}")
