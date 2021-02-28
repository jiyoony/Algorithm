#네 번째 점
location=[]
for _ in range(3):
    x,y=map(int,input().split())
    location.append((x,y))

if (location[0][0]== location[1][0]):
    sqx=location[2][0]
elif(location[1][0]==location[2][0]):
    sqx=location[0][0]
else:
    sqx=location[1][0]

if (location[0][1]== location[1][1]):
    sqy=location[2][1]
elif(location[1][1]==location[2][1]):
    sqy=location[0][1]
else:
    sqy=location[1][1]


# print(str(sqx)+" "+str(sqy))
print(sqx, end=" ")
print(sqy)
