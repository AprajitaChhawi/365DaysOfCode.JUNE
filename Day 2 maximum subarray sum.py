t=int(input())
while t:
    t=t-1
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m=min(l)
    if(m>=0):
        s=sum(l)
        print(k*s)
    else:
        l1=l[:]
        sublist=[]
        for i in range(len(l1)+1):
            for j in range(i+1,len(l1)+1):
                sublist.append((sum(l1[i:j])))
        print(sublist)
        print(max(sublist)+sum(l)*(k-1))
                
