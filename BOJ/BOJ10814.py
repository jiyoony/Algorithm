#나이순 정렬
n=int(input())
members=[]
for _ in range(n):
    age,name=input().split()
    age=int(age)
    members.append((age,name))

members.sort(key=lambda x: (x[0]))

for member in members:
  print(member[0],member[1])
