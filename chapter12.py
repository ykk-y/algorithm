'''
7

'''
def solution_7():
    lucky = input()
    cnt = int(len(lucky)/2)
    left=0
    right=0
    for i in range(cnt):
        left += int(lucky[i])
        right += int(lucky[-1-i])
    #왼쪽 더하기
    #오른쪽 더하기
    #출력
    if left == right:
        print('LUCKY')
    else:
        print('READY')
solution_7()