class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        
        reverse(nums.begin() + (n-k), nums.end()); // 1 2 3 4 7 6 5
        
        reverse(nums.begin(), nums.begin() + (n - k));
        
        reverse(nums.begin(), nums.end());
    }
};