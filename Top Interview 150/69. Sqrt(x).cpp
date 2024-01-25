class Solution {
public:
    long long int mySqrt(long long int x) {
        long long int left = 0, right = x, ans = 0;
        
        while(left <= right){
            long long int mid = left + ((right - left) / 2);
            if(mid * mid > x){
                right = mid - 1;
            }
            else if(mid * mid < x){
                left = mid + 1;
                ans = mid;
            }
            else{
                return mid;
            }
        }
        return ans;
    }
};
