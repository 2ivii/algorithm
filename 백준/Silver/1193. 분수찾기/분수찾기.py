import sys

input = sys.stdin.readline

n=int(input())
cnt=i=j=1
while cnt<n:
    if i==1 and j==1:
        j+=1
    elif i==1 and j%2==0:
        i+=1
        j-=1
    elif i==1 and j%2!=0:
        j+=1
    elif j==1 and i%2==0:
        i+=1
    elif j==1 and i%2!=0:
        j+=1
        i-=1
    elif i%2==j%2:
        i-=1
        j+=1
    elif i%2!=j%2:
        i+=1
        j-=1
    cnt+=1

print(f"{i}/{j}")