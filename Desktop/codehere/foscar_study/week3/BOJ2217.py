#로프
n=int(input())
k=[]
for i in range(n):
    k.append(int(input()))
k.sort()
weight=0
for i in range(n):
    if weight<k[i]*(n-i):
       weight=k[i]*(n-i)
print(weight)
