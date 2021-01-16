#평균점수
l=[]
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))

amount=0
for i in range(5):
    if l[i]<40:
        l[i]=40
    amount+=l[i]
avg=int(amount/5)
print(avg)
