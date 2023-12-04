//problem link : https://practice.geeksforgeeks.org/problems/largest-prime-factor2601/1
//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public: 
    long long int largestPrimeFactor(int n){
        // code here
        long long int ans = 0;
        for(long long int i = 2; i * i <= n; i++){
            if(n % i == 0){
                ans = max(ans, i);
                while(n % i == 0){
                    n /= i;
                }
            }
        }
        if(n > 1)
            ans = n;
        return ans;
        
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.largestPrimeFactor(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends
