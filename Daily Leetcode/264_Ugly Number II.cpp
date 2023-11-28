class Solution {
public:
    int nthUglyNumber(int n) {
        if(n == 1)
            return 1;
        vector<int>ug(n);
        ug[0] = 1; //from the given test cases it's confirm.
        int i2 = 0, i3 = 0, i5 = 0;
        for(int i = 1; i < n; i++){
            //minn = min(a, min(b,c))
            ug[i] = min(2 * ug[i2], min(3 * ug[i3], 5 * ug[i5]));
            if(ug[i] == 2 * ug[i2]){
                i2++;
            }
            if(ug[i] == 3 * ug[i3]){
                i3++;
            }
            if(ug[i] == 5 * ug[i5]){
                i5++;
            }
        }
        return ug[n - 1];
    }
};