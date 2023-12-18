class Solution {
public:
    double myPow(double x, int n) {

        double ans = 1;
        int tempn = n;
        if(n < 0){
            n = abs(n);
        }
        while(n > 0){
            if(int(n) % 2 ==  1){
                ans *= x;
            }
            x *= x;
            n /= 2;
        }
        cout << ans;
        if(tempn < 0){
            return 1/ans;
        }
        return ans;
        
    }
};