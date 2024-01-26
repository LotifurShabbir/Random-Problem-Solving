class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        int ans = nums.size();
        // if(nums.size() <= 1){
        //     return 0;
        // }
        while(l <= r){
            int mid = l + ((r - l) / 2);
            if(nums[mid] > target){
                r = mid - 1;
                ans = mid;
            }
            else if(nums[mid] < target){
                l = mid + 1;
                ans = mid + 1;
            }
            else{
                return mid;
            }
        }
        return ans;
    }
};