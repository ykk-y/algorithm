'''
4 6
19 15 10 17
'''
N, M=map(int,input().split())
x=list(map(int,input().split()))

def solution_1():
    pass
    x.sort(reverse=True)
    i=1
    while True:
        result = 0
        H=x[i]
        for j in range(i):
           result+=x[j]-H
        if result>=M:
            return H
        i+=1

print(solution_1())