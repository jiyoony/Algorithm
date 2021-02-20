#좌표 정렬하기
n=int(input())
line=[]

for _ in range(n):
    x,y=map(int,input().split())
    line.append((x,y))

line.sort(key=lambda x:(x[1],x[0]))
# -를 붙이면 역순으로 정렬
for i in range(len(line)):
    print(line[i][0],end=" ")
    print(line[i][1])
