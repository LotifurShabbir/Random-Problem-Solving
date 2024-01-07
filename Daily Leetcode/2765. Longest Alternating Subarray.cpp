class Solution {
public:
    int alternatingSubarray(vector<int>& nums) {
        int maxLen = INT_MIN, maxCurr = 1;
        bool plusOne = true;
        for(int i = 0; i < nums.size() - 1; i++)
        {
            if(nums[i + 1] - nums[i] == 1 && plusOne)
            {
                maxCurr++;
                plusOne = false;
            }
            else if(nums[i + 1] - nums[i] == -1 && !plusOne)
            {
                maxCurr++;
                plusOne = true;
            }
            else
            {
                maxLen = max(maxLen, maxCurr);
                if(nums[i + 1] - nums[i] == 1)
                {
                    maxCurr = 2;
                    plusOne = false;
                }
                else
                {
                    maxCurr = 1;
                    plusOne = true;
                }
            }
        }
        
        
        int res = max(maxLen, maxCurr);
        
        if(res == 1)
            return -1;

        return res;
    }
};