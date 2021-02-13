#덩치
n=int(input())
dungchi=[]

for i in range(n):
    x,y=map(int,input().split(" "))
    dungchi.append((x,y))

for i in dungchi:
    //i=(x,y) 쌍임
    rank = 1
    for j in dungchi:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=" ")
