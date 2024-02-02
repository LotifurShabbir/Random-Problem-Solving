class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        vector<int>v;
        
        for(int i = 0; i < m; i++){
            v.push_back(nums1[i]);
        }
        
        for(int i = 0; i < n; i++){
            v.push_back(nums2[i]);
        }

        sort(v.begin(), v.end());
        // for(auto x : v){
        //     cout << x << endl;
        // }

        int final_vec = v.size();
        //cout << final_vec << endl;
        
        double result = 0;
        if(final_vec % 2 == 0){
            result = v[(final_vec/2) - 1] + v[(final_vec/2)];
            result = (result / 2);

        }
        else if(final_vec % 2 != 0){
            result = v[((final_vec + 1) / 2) - 1];
        }
        return result;
    }
};