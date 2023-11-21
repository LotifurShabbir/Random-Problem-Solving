class Solution {
public:
    int countPrimes(int n) {
        long long int ans = 0;
        if(n < 2){
            return 0;
        }
        vector<bool>isPrime(n, true);
        isPrime[0] = isPrime[1] = false;
        for(long long int i = 2; i < n; i++){
            if(isPrime[i] == true){
                for(long long int j = i * 2; j < n; j += i){
                    isPrime[j] = false;
                }
            }
        }
        for(auto x : isPrime){
            if(x == true){
                ans++;
            }
        }
        return ans;        
    }
};