class Solution:
    #User function Template for python3
    
    ##Complete this function
    #Function to find index of element x in the array if it is present.
    def closer(self, arr, n,  x):
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==x:
                return mid
            elif mid>0 and arr[mid-1]==x:
                return mid-1
            elif mid<n and arr[mid+1]==x:
                return mid+1
            elif arr[mid]>x:
                high=mid-1
            else:
                low=mid+1
        return -1
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
    
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            X=int(input())
            obj = Solution()
            res=obj.closer(A,N,X)
            print(res)
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
