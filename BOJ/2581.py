import sys
M=int(sys.stdin.readline().strip())
N=int(sys.stdin.readline().strip())
min_=10001
sum_ = 0
for num in range(M,N+1):
    if num==1:#1에 대한 처리가 필요
        continue
    res=False#소수임
    for i in range(2,num):
        if num%i==0:#나뉘면
            res=True#소수아님
            break
    if res==False:#소수라면
        min_=min(min_,num)
        sum_+=num
if sum_==0:
    print(-1)
else:
    print(sum_)
    print(min_)