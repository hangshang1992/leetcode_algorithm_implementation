class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> p(m+1, vector<int>(n+1));
        for (int i = 0; i <= m;i++){
            p[i][0] = i;
        }
        for (int j = 0; j <= n;j++){
            p[0][j] = j;
        }
        for (int i = 1; i<= m; i++){
            for (int j = 1; j <= n; j++){
                if (word1[i-1] == word2[j-1]){
                    p[i][j] = p[i-1][j-1];
                }
                else{
                    p[i][j] = 1 + min({p[i-1][j], p[i][j-1], p[i-1][j-1]});
                }
            }
        }
        return p[m][n];
    }
};
