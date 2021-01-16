#셀프넘버
def self(n):
    a=[]
    b=n+int(n/10)+n%10
    a.append(b)
    retrun list(a)
for i in range(1,10001):
    self(i)

result=[i for i is not in range(1,10001)]

self=set(range(1,10001))
generate=set()
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    getnerate.add(i)
