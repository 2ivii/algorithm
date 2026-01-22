import sys

input = sys.stdin.readline

n=int(input())
count=0
for i in range(1,n+1):
    hundred=i//100
    ten=(i%100)//10
    one=i%10
    if hundred!=0 and hundred-ten == ten-one:
        count+=1
    elif hundred ==0 or (hundred==0 and ten==0):
        count+=1

sys.stdout.write(str(count))