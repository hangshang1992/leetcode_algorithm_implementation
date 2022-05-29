class Solution {
public:
    int n,m;
    int numIslands(vector<vector<char>>& grid) {
        m = grid.size();
        n = grid[0].size();
        vector<vector<int>> visited(m, vector<int>(n, 0));
        int ans = 0;
        for(int i = 0;i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1' and !visited[i][j]){
                    ++ans;
                    dfs(grid, visited, i, j);
                }
            }
        }
        return ans;
    }
    
    // void dfs(vector<vector<char>>& grid, vector<vector<int>>& visited,int i,int j) {
    //     if(i < 0 || i > m - 1 || j < 0 || j > n - 1 || grid[i][j] == '0')return;
    //     visited[i][j] = 1;
    //     visited[i][j] = 1;
    //     if (i-1>=0 and !visited[i-1][j]){
    //         dfs(grid, visited, i-1, j);
    //     }
    //     if (i+1<= grid.size() - 1 and !visited[i+1][j]){
    //         dfs(grid, visited, i+1, j);
    //     }
    //     if(j-1>=0 and !visited[i][j-1]) dfs(grid,visited,i,j - 1);
    //     if(j+1<=grid[0].size() - 1 and !visited[i][j+1]) dfs(grid,visited,i,j + 1);
    // }

    void dfs(vector<vector<char>>& grid, vector<vector<int>>& visited, int i, int j){
        if (i<0 or i >= grid.size() or j < 0 or j >= grid[0].size() or grid[i][j] == '0'){
            return;
        }
        visited[i][j] = 1;
        if (i-1>=0 and !visited[i-1][j]){
            dfs(grid, visited, i-1, j);
        }
        if (i+1<= grid.size() - 1 and !visited[i+1][j]){
            dfs(grid, visited, i+1, j);
        }
        if(j-1>=0 and !visited[i][j-1]){
            dfs(grid, visited, i , j-1);
        }
        if(j+1<=grid[0].size() - 1 and !visited[i][j+1]){
            dfs(grid, visited, i, j+1);
        }
        return ;
    }
};
