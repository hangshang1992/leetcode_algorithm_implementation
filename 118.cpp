class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> np;
        np.resize(numRows);
        for(int i = 0; i < numRows; i++){
            np[i].resize(i+1);
            np[i][0] = 1;
            for ( int col = 1; col <= i; col++){
                np[i][col] = np[i-1][col-1] + (col < i? np[i-1][col]:0);
            }
        }
        return np;
    }
};
