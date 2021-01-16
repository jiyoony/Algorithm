#단어공부
a=input().upper()
c=list(set(a))
b=list()
for i in c:
    b.append(a.count(i))

if (b.count(max(b))>=2):
    print("?")
else:
    print(c[(b.index(max(b)))])
