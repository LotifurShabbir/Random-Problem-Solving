class Solution {
public:
    int commonFactors(int a, int b) {
        int ans = 0; int rangee = max(a,b);
        for(int i = 1; i <= rangee; i++){
            if(a % i == 0 && b % i == 0){
                ans++;
            }
        }
        return ans;
    }
};