class Solution {
public:
    int maxPoints(vector<vector<int>>& p) {
        if (p.size() <= 2) {
            return p.size();
        }

        int ans = 2;
        int n = p.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int total = 2;
                for (int k = 0; k < n; k++) {
                    if (k != i && k != j) { // because i take 2 pointer already
                                            // (x1,y1) and (x2,y2)
                        if ((p[j][1] - p[i][1]) * (p[k][0] - p[i][0]) ==
                            (p[k][1] - p[i][1]) * (p[j][0] - p[i][0])) { //i = x1, j = x2, k = x3
                            total++;
                        }
                    }
                }
                ans = max(ans, total);
            }
        }

        return ans;
    }
};