class Solution {
public:
    int candy(vector<int>& arr) {
        long long int n = arr.size();
        vector<long long int>candy(n, 1);
        
        //from left to right
        for(long long int i = 1; i < n; i++){
            if(arr[i-1] < arr[i]){
                candy[i] = candy[i-1] + 1; //*** MADE A MISTAKE HERE***
            }
        }
        //from right to left
        for(long long int i = n - 2; i >= 0; i--){
            if(arr[i] > arr[i+1]){ // 5 5 6 1 4 6
                candy[i] = max(candy[i], candy[i+1] + 1);
            }
        }
        
        long long int ans = 0;
        for(auto x : candy){
            ans += x;
        }

        return ans;
    }
};