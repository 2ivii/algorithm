n = int(input())
sequence = []
stack = []
result = []
current = 1

for _ in range(n):
    x = int(input())
    sequence.append(x)
    
for num in sequence:
    while current<=num:
        stack.append(current)
        result.append('+')
        current+=1
    
    if stack[-1] == num:
        result.append('-')
        stack.pop()
    
    else:
        print("NO")
        exit(0)
    

for i in range(len(result)):
    print(result[i])
