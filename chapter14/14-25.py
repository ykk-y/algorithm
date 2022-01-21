'''
다 세어야 하는데 for문은 1개만 써야할것 같음..
list의 count! count는 내림차순
sort 다시...

5
2 1 2 6 2 4 3 3
'''

N=int(input())
x=list(map(int,input().split()))
user=len(x)
result=[]
for i in range(1,N+1):
    count = x.count(i)
    result.append((i,count/user))
    user-=count

result.sort(key = lambda x: (-x[1],x[0]))
for i in range(N):
    print(result[i][0])



