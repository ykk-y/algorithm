'''
while을 써서 큰값을 만날 때 조건을 걸어주었는데
for로 전체를 다 보아야 했음
dp여서 전체를 다 보면 낭비 아닌가 했는데.. LIS 문제라고 함
'''

N=int(input())
x=list(map(int,input().split()))
y=[1]*(N)
for i in range(1,N):
    for j in range(i):
        if x[j]>x[i]:
            y[i]=max(y[j]+1,y[i])
print(N-max(y))
'''
7
15 11 4 8 5 2 4
'''