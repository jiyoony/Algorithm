#숫자의 개수
a=int(input())
b=int(input())
c=int(input())

d=a*b*c
str(d)
num=list(map(int,str(d)))
for i in range(10):
    print(num.count(i))
