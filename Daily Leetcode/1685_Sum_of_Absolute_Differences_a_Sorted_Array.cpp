class Solution {
public:
    vector<int>getSumAbsoluteDifferences(vector<int>& nums) {
        vector<int>ans;
        long long int totalSum = 0;
        int n = nums.size();
        for(auto x : nums){
            totalSum += x;
        }
        int leftSum = 0;
        for(int i = 0; i < n; i++){
            int Left = (nums[i] * i) - leftSum;
            int Right = totalSum - leftSum - nums[i]*(n-i);
            leftSum += nums[i];
            ans.push_back(Left + Right);
        }
        return ans;
    }
};
// Input: nums = [2,3,5]
// Output: [4,3,5]