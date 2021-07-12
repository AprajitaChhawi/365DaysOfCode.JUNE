def segregate(l,n):
    i=-1
    for j in range(0,n):
        if l[j]<0:
            i=i+1
            l[i],l[j]=l[j],l[i]
    return l
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    l=segregate(l,n)
    print(l)
