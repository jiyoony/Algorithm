#직사각형에서 탈출
x,y,w,h=map(int,input().split())
lenn=[]
lenn.append(x)
lenn.append(y)
lenn.append(w-x)
lenn.append(h-y)
lenn.sort()
print(lenn[0])
