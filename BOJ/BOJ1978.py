#소수찾기
n=int(input())
cnt=0
nums=[int(i) for i in input().split(" ")]
for num in nums:
    for i in range(2,num+1):
        if num %i==0:
            if i !=num:
                break
            else:
                cnt+=1
print(cnt)
