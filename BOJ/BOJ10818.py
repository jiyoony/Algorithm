#최소,최대
n=int(input())
data=list(map(int,input().split()))
data.sort()
print(data[0],data[n-1])
