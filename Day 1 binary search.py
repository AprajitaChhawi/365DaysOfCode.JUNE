def BinarySearch(l,k,low,high):
    if(low>high):
        return -1
    mid=int((low+high)/2)
    if(l[mid]==k):
        return 1
    elif(l[mid]>k):
        return BinarySearch(l,k,low,mid-1)
    else:
        return BinarySearch(l,k,mid+1,high)
    
try:
    t=int(input())
    while t:
        low=0
        t=t-1
        n,k=map(int,input().split())
        high=n
        l=list(map(int,input().split()))
        k=BinarySearch(l,k,low,high)
        print(k)
except Exception:
    pass;
        
