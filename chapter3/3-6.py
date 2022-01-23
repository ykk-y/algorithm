from collections import deque
'''
5
3 1 2
'''
k=int(input())
food_times=list(map(int,input().split()))
print(food_times)
l=len(food_times)
food_index=[i+1 for i in range(l)]
print(food_index)
food=list(zip(food_times,food_index))
print(food)

queue=deque(food)
print('시작')
cnt = 0
while cnt != k:
    tmp1,tmp2=queue.popleft()
    if tmp1!=0:
        tmp1-=1
        cnt+=1
    queue.append((tmp1,tmp2))
    print(queue)
tmp1,tmp2=queue.popleft()
print(tmp2)