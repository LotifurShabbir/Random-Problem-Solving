class Solution {
public:
    int singleNumber(vector<int>& nums) {
        long int ans = 0;
        long int n = nums.size();
        for(long long int i = 0; i < n; i++){
            ans = ans ^ nums[i];
        }
        return ans;
        
    }
};