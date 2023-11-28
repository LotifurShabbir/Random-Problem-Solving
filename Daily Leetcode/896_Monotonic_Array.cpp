class Solution {
    bool checkingIncr(vector<int>n){
    for(int i = 1; i < n.size(); i++){
        if(n[i] < n[i-1]){
            return false;
        }
    }
    return true;
}
bool checkingDecr(vector<int>n){
    for(int i = 1; i < n.size(); i++){
        if(n[i] > n[i-1]){
            return false;
        }
    }
    return true;
}
public:
    
    bool isMonotonic(vector<int>& nums) {
        return checkingDecr(nums) || checkingIncr(nums);
    }
};
