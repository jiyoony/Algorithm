#알람시계
h,m=map(int,input().split())

if (h>0 and m<45):
    print("%d %d" %(h-1,m+15))
elif (h==0 and m<45):
    print("%d %d" %(23,m+15))
else:
    print("%d %d" %(h,m-45))
