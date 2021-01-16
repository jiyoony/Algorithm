#셀프넘버
#인터넷 보고 한거
def d(num):
    result = num
    for n in str(num):
        result+=int(n)
    return result
arr=[]
for i in range(1,10000):
    next_num=d(i)
    if next_num <100000:
        arr.append(next_num)
    if i not in arr:
        print(i)
