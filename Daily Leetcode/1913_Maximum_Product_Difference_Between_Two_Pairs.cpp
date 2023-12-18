class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        
        sort(nums.rbegin(), nums.rend());
        return (nums[0] * nums[1]) - (nums[nums.size() - 1] * nums[nums.size() - 2]);
        // [9,9,5,2,1]
        
    }
};