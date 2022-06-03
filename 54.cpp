class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 or matrix[0].size() == 0){
            return {};
        }
        int di = 0, dj = 1;
        int i = 0, j = 0;
        vector<int> res;
        for(int k = 0; k < matrix.size() * matrix[0].size(); k++){
            res.push_back(matrix[i][j]);
            matrix[i][j] = 0;
            if(matrix[(i+di)%matrix.size()][(j+dj)%matrix[0].size()] == 0){
                int tmp = di;
                di = dj;
                dj = -tmp;
            }
            i = i + di;
            j = j + dj;
        }
        return res;
    }
};
