#include<iostream>
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        for (int i = 0; i < grid.size(); i++){
            for (int j = 0; j < grid[0].size(); j++){
                // cout << i << " " << j << " d ";
                if (i == 0 and j > 0){
                    grid[i][j] += grid[i][j-1];
                }
                else if (j == 0 and i > 0){
                    grid[i][j] += grid[i-1][j];
                }else if (i>0 and j > 0){
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
                }
            }
        }
        return grid[grid.size() - 1][grid[0].size() - 1];
    }
};
