class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int>freqs;        
        unordered_map<char,int>freqt;
        for(auto x : s){
            freqs[x]++;
        }
        for(auto x : t){
            freqt[x]++;
        }
        return freqs == freqt;
    }
};