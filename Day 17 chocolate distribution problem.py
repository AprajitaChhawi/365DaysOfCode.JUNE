#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        res=A[M-1]-A[0]
        i=1
        while(i+M-1<N):
            res=min(res,A[i+M-1]-A[i])
            i=i+1
        return res

        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends
