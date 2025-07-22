n=int(input())
c=1000-n
count=0
coin=[500,100,50,10,5,1]
for i in range(0,6):
    while c>=coin[i]:
        c-=coin[i]
        count+=1

print(count)