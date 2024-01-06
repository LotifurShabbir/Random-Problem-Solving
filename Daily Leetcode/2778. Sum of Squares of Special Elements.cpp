class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int n = nums.size();
        long long int sum = 0;
        for(int i = 0; i < n; i++){
            cout << nums[i];
            if(n % (i + 1) == 0){
                sum += nums[i] * nums[i];
            }
        }
        return sum;
    }
};