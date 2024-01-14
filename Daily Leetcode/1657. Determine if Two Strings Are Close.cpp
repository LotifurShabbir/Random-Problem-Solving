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

////python solution
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        dic1 = Counter(word1)
        dic2 = Counter(word2)

        if dic1 == dic2:
            return True

        keyCount, value = [], []
        for key, val in dic1.items():
            keyCount.append(key)
            value.append(str(val))

        keyCount2, value2 = [], []
        for key, val in dic2.items():
            keyCount2.append(key)
            value2.append(str(val))
        
        keyCount.sort()
        value.sort()
        keyCount2.sort()
        value2.sort()

        return keyCount == keyCount2 and value == value2