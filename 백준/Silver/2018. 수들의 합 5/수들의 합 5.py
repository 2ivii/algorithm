import sys

input=sys.stdin.readline

n=int(input())
count=1
start=1
end=1
sum=0
while end<=n:
    if sum<n:
        sum+=end
        end+=1
    elif sum>n:
        sum-=start
        start+=1

    elif sum == n:
        # print("start랑 end는",start,end)
        count+=1
        sum -= start
        start += 1
sys.stdout.write(str(count))