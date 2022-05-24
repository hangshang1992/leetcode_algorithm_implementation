class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> np;
        np.resize(rowIndex + 1);
        for (int i = 0; i < rowIndex + 1; i++){
            np[i].resize(i+1);
            np[i][0] = 1;
            for(int col = 1 ; col <= i; col++){
                np[i][col] = np[i-1][col-1] + (col < i ? np[i-1][col] : 0);
            }
        }
        return np[rowIndex];
    }
};
