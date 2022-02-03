tmp=input()
x,y=ord(tmp[0])-ord('a'),int(tmp[1])-1
dir1=[(0,2),(0,-2)]
dir2=[(1,0),(-1,0)]

dir3=[(2,0),(-2,0)]
dir4=[(0,1),(0,-1)]


def sol():
    cnt=0
    if x<0 or x>=8 or y<0 or y>=8:
        return
    for i in range(2):
        for j in range(2):
            if y+dir1[i][1]>=0 and y+dir1[i][1]<8:
                if x+dir2[j][0]>=0 and x+dir2[j][0]<8:
                    cnt +=1
    for k in range(2):
        for l in range(2):
            if y+dir3[k][0]>=0 and y+dir3[k][0]<8:
                if x+dir4[l][1]>=0 and x+dir4[l][1]<8:
                    cnt +=1
    return cnt
print(sol())