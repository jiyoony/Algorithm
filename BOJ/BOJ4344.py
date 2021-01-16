#평균은 넘겠지
'''
c=int(input())
avg=0
score=[]
for i in range(c):
    n=int(input())
     for j in range(n):
        score=list(map(int,input().split()))
        for k in range(n):
             whole+=score[k]
        avg=whole/n
        scorelist=[num for num in score if num > avg]
        print('%.3f%' %len(scorelist)/ n *100+'%')
'''

for i in range(int(input())):
    sco_list=list(map(int,input().split()))
    avg=sum(sco_list[1:])/sco_list[0]
    count=0
    for j in sco_list[1:]:
        if j>avg:
            count+=1
    print('%.3f' %(count/sco_list[0]*100)+'%')
