class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int sz = words.size();
        string temp = "";
        for (const string& word : words) {
            temp += word;
        }
        unordered_map<char, int> charCount;
        for (char c : temp) {
            charCount[c]++;
        }
        for (const auto& entry : charCount) {
            if (entry.second % sz != 0) {
                return false;
            }
        }
        return true;
    }
};
