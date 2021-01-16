#분수찾기
#모름
x=int(input())
stage,key_x=1,1
while key_x+stage<=x:
    key_x+=stage
    stage+=1
step=x-key_x
first,second=step+1,stage-step
if stage%2==0:
    print('{}/{}'.format(first,second))
else:
    print('{}/{}'.format(second,first))
