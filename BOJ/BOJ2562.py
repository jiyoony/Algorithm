#최댓값
data=[]
for i in range(9):
    data.append(int(input()))
newdata=sorted(data)
print(newdata[8])
print(data.index(newdata[8])+1)
