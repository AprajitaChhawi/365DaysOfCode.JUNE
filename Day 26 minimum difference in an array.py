#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

class Solution:
    #Function to find minimum difference between any pair of elements in array.
	def MinimumDifference(self, arr, n):
	    arr.sort()
	    res=arr[1]-arr[0]
	    for i in range(2,n):
	        res=min(res,arr[i]-arr[i-1])
	    return res
		# Code here

#{ 
#Driver Code Starts.
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.MinimumDifference(arr,n)
        print(ans)
#} Driver Code Ends
