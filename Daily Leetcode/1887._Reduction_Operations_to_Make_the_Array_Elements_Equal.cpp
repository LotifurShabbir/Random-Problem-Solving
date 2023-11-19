class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int ans = 0;
        int prv = nums[0];
        int n = nums.size();
        for(int i = 1; i < n; i++){
            if(prv != nums[i]){
                ans += n - i;
                prv = nums[i];
            }
        }
        return ans;
        
    }
};