class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.size() != word2.size()) {
            return false;
        }

        unordered_map<char, int> count1, count2;
        unordered_set<char> unique_c1, unique_c2;

        for (auto c : word1) {
            count1[c]++;
            unique_c1.insert(c);
        }

        for (char c : word2) {
            count2[c]++;
            unique_c2.insert(c);
        }

        if (count1.size() != count2.size() || unique_c1 != unique_c2) {
            return false;
        }

        vector<int> values1, values2;

        for (auto i : count1) {
            values1.push_back(i.second);
        }

        for (auto i : count2) {
            values2.push_back(i.second);
        }

        sort(values1.begin(), values1.end());
        sort(values2.begin(), values2.end());

        return values1 == values2;
    }
};
