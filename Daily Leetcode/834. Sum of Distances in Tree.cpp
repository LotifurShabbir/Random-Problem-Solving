class Solution {
    int subtree[30005];
    vector<int>next[30005];
    int visited[30005];
    vector<int>rets;
    int n;
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        this->n = n;
        rets.resize(n, 0);
        for(auto&edge:edges){
            next[edge[0]].push_back(edge[1]);
            next[edge[1]].push_back(edge[0]);
        }    
        visited[0] = 1;
        dfs(0);
        for(int i = 1; i < n; ++i) visited[i] = 0;
        rets[0] = dfs2(0);
        for(int i = 1; i < n; ++i) visited[i] = 0;
        dfs3(0);

        return rets;
    }
    
    int dfs(int cur){
        int sum = 1;
        for(auto x: next[cur]){
            if(visited[x] == 1) continue;
            visited[x] = 1;
            sum += dfs(x);
        }
        subtree[cur] = sum;
        return sum;
    }
    
    int dfs2(int cur){
        int sum = 0;
        
        for(int x : next[cur]){
            if(visited[x] == 1) continue;
            visited[x] = 1;
            sum += dfs2(x);
        }
        sum += subtree[cur] - 1;
        return sum;
    }
    void dfs3(int cur){        
        for(int x : next[cur]){
            if(visited[x] == 1) continue;
            visited[x] = 1; 
            int b = subtree[x];
            int a = n - b; 
            rets[x] = rets[cur] + a - b;
            dfs3(x);
        }
        return; 
    }
    
};