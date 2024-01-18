class Solution {
public:
    int climbStairs(int n) {
        int ans = 1, cur = 0, back = 0;
        for(int i = 0; i < n; i++){
            back = ans + cur;
            cur = ans;
            ans = back;
        }
        return ans;
        
    }
};