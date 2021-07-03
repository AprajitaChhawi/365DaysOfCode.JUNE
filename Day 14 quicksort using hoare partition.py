#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if(low<high):
            p=self.partition(arr,low,high)
            self.quickSort(arr,low,p)
            self.quickSort(arr,p+1,high)
        return arr
        # code here
    
    def partition(self,arr,low,high):
        pivot=arr[low]
        i=low-1
        j=high+1
        while(True):
            i=i+1
            while(arr[i]<pivot):
                i=i+1
            j=j-1
            while(arr[j]>pivot):
                j=j-1
            if(i>=j):
                return j
            arr[i],arr[j]=arr[j],arr[i]
        # code here
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
