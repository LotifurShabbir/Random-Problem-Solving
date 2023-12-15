class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        //0 1 3
        long long int all_sum = n*(n+1)/2;
        // cout << all_sum << endl;
        long long int array_sum = 0;
        for(int i = 0; i < nums.size(); i++){
            array_sum += nums[i];
        }

        return all_sum - array_sum;
           
    }
};