#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        while(l<=r):
            p=self.partition(arr,l,r)
            if p==k-1:
                return arr[p]
            elif p>k-1:
                r=p-1
            else:
                l=p+1
    def partition(self,arr,l,r):
        pivot=arr[r]
        i=l-1
        for j in range(l,r):
            if arr[j]<pivot:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[r]=arr[r],arr[i+1]
        return (i+1)
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends
