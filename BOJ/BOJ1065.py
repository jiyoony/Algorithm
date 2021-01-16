# -*- coding: utf-8 -*-
#한수
def minus(w):
    count=0
    for i in range(1,w+1):
        if i<100:
            count+=1
        else:
            p=str(i)
            if p[1] != '0' :
                w1=i//100
                w2=(i-w1*100)//10
                w3=(i-w1*100)%10
                if (w1-w2)==(w2-w3):
                    count+=1
    return count
print(minus(int(input())))
