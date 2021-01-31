#피보나치 수 2
n=int(input())
arr=[0 for i in range(n+1)]
arr[1]=1
if n>1:
    arr[2]=1
def fibo(k):
    if (arr[k]!=0):
         return arr[k]
    else:
        arr[k]= fibo(k-1)+fibo(k-2)
        return arr[k]

print(fibo(n))
