#바이러스
n=int(input())
connect=int(input())
adj=[[]for _ in range(n+1)]
liste=[]
check=[0 for _ in range(n+1)]
for i in range(connect):
    k,p=map(int,input().split())
    adj[k].append(p)
    adj[p].append(k)

def dfs(graph):
    for j in graph:
        liste.extend(adj[j])
        check[j]=1
        for i in adj[j]:
            liste.extend(adj[i])
            if (check[i]==0):
                check[i] = 1
                dfs(adj[i])

dfs(adj[1])

sete=set(liste)
print(len(sete)-1)
