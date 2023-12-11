class Solution {
public:
    int numberOfWays(string corridor) {
        int mod = 1000000007;

        long long int count = 0;
        for(auto x : corridor){
            if(x == 'S'){
                count++;
            }
        }
        if(count < 2 || count % 2 == 1){
            return 0;
        }

        vector<int>sp;
        int n = corridor.size();
        for(int i = 0; i < n; i++){
            if(corridor[i] == 'S'){
                sp.push_back(i);
            }
        }
        // for(auto x : sp){
        //     cout << x;
        // }
        long long int ans = 1;
        for(int i = 1; i < sp.size() - 1; i += 2){
            // cout << sp[i];
            ans = (ans * (sp[i + 1] - sp[i])) % mod;
        }

        return ans;
    }
};