'''
5 3
1 2 5 4 3
5 5 6 6 5
'''

N,K=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

x.sort()
y.sort(reverse=True)
print(x)
print(y)

x[:K],y[:K]=y[:K],x[:K]
print(x)
print(y)
print(sum(x))