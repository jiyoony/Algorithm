#소트인사이드
n=input()
nums=[]
for i in range(len(n)):
    nums.append(n[i])
nums.sort(reverse=True)
for i in range(len(n)):
    print(nums[i],end='')