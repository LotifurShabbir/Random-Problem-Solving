class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (auto x : nums) {
            freq[x]++;
        }
        vector<pair<int, int>> freqVec(freq.begin(), freq.end());

        
        sort(freqVec.begin(), freqVec.end(), [](const auto& a, const auto& b) {
            return a.second > b.second;
        });

        vector<int> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(freqVec[i].first);
        }

        return ans;
    }
};
