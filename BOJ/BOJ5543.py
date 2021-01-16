#상근날드
bug1=int(input())
bug2=int(input())
bug3=int(input())
bev1=int(input())
bev2=int(input())

if bev1>bev2:
    lowbev=bev2
else:
    lowbev=bev1

if bug1>bug2:
    lowbug=bug2
else:
    lowbug=bug1
if lowbug>bug3:
    lowbug=bug3

print(lowbug+lowbev-50)
