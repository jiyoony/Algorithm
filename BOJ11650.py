#좌표 정렬하기
n=int(input())
line=[]

for _ in range(n):
    x,y=map(int,input().split())
    line.append((x,y))

line.sort()

for i in range(len(line)):
    print(line[i][0],end=" ")
    print(line[i][1])
