n=int(input())
x=[ 0 for i in range(1001) ]
x[1]=1
j=2
for i in range(2,1001):
    if i%5 ==0 or i%3==0 or i%2==0:
        x[j]=i
        j+=1

print(x[n])
