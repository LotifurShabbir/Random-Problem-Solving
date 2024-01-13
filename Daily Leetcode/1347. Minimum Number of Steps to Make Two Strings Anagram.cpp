class Solution {
public:
    int minSteps(string s, string t) {
        unordered_map<char, int> sc;
        unordered_map<char, int> tc;

        for (char ch : s) {
            sc[ch]++;
        }

        for (char ch : t) {
            tc[ch]++;
        }

        int ans = 0;

        for (auto i : sc) {
            char key = i.first;
            int value = i.second;

            if (tc.find(key) != tc.end()) {
                if (sc[key] > tc[key]) {
                    ans += sc[key] - tc[key];
                }
            } else {
                ans += sc[key];
            }
        }

        return ans;
    }
};