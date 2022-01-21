'''
for를 여러번 쓸수는 없는것 같은데 정렬을
'''
import heapq

N=int(input())
x=[]
for i in range(N):
    x.append(int(input()))
x.sort()

tmp=x[0]
result=0
for i in range(1,N):
    tmp = tmp + x[i]
    result+=tmp
print(result)


