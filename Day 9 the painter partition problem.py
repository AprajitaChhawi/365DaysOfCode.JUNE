#User function Template for python3

class Solution:
    def minTime (self, arr,n,k):
        low=max(arr)
        high=sum(arr)
        res=0
        while(low<=high):
            mid=(low+high)//2
            if(self.isFeasible(arr,n,k,mid)):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    def isFeasible(self,arr,n,k,ans):
        req=1
        s=0
        for i in range(n):
            if (s+arr[i])>ans:
                req=req+1
                s=arr[i]
            else:
                s=s+arr[i]
        return (req<=k)
        #code here
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends
