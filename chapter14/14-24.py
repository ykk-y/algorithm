'''
4
5 1 7 9
'''
N=int(input())
x=list(map(int,input().split()))

result=[]
for i in range(N):
    sum=0
    for j in range(N):
        sum += abs(x[j]-x[i])
    result.append((sum,x[i]))

result.sort(key=lambda x: (x[0],x[1]))
print(result[0][1])
