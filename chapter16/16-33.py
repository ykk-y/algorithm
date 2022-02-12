N=int(input())
'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''
'''
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
'''
'''
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6
'''
'''
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
'''

x=[0]*(N+1)
T=[]
P=[]
for i in range(N):
    a,b=map(int,input().split())
    T.append(a)
    P.append(b)

for j in range(1,N+1):
    if j-1+T[j-1]>N:
        break
    if x[j]!=0: #채워진 경우
        if T[j-1] == 1 :
            x[j] = max(x[j], x[j - 2] + P[j-1])
        else:
            x[j-1+T[j-1]] = max(x[j - 2] + P[j-1],x[j-1+T[j-1]])
    else: #비어있는 경우
        if T[j-1] == 1 :
            x[j] = max(x[j], x[j - 1] + P[j-1])
        else:
            p=j-1+T[j-1]
            x[j-1+T[j-1]] = max(x[j - 1] + P[j-1],x[j-1+T[j-1]])

print(max(x))