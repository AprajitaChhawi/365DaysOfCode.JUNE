#User function Template for python3

class Solution:
    def findSubArraySum(self, Arr, N, k):
        m={}
        c=0
        s=0
        for i in range(N):
            s=s+Arr[i]
            if s==k:
                c=c+1
            if s-k in m:
                c=c+m[s-k]
            if s not in m:
                m[s]=1
            else:
                m[s]=m[s]+1
        return c
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends
