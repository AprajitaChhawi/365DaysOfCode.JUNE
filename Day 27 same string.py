#User function Template for python3
class Solution:
    def count(self, S):
        n=len(S)
        l=[]
        for i in S:
            if i=='B' :
                if len(l)>0 and l[-1]=='A':
                    l.pop()
                else:
                    l.append(i)
            else:
                l.append(i)
        return len(l)//2
            
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.count(S)
        print(ans)
# } Driver Code Ends
