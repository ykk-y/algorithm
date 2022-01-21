'''
for를 여러번 쓸수는 없는것 같은데 정렬을
'''
import heapq

def solution_2():
    N = int(input())
    x = []
    result=0
    for i in range(N):
        heapq.heappush(x,int(input()))

    while len(x) != 1:
        one = heapq.heappop(x)
        two = heapq.heappop(x)
        sum = one+two
        result += sum
        heapq.heappush(x,sum)
    print(result)



def solution_1():
    N = int(input())
    x = []
    for i in range(N):
        x.append(int(input()))
    x.sort()

    tmp = x[0]
    result = 0
    for i in range(1, N):
        tmp = tmp + x[i]
        result += tmp
    print(result)



