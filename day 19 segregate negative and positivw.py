def segregate(arr,n):
    i=-1
    for j in range(0,n):
        if arr[j]<0:
            i=i+1
            a[i],a[j]=a[j],a[i]
    return a
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    l=segregate(l,n)
    print(l)
