class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (board.size() == 0 or board[0].size() == 0){
            return false;
        }
        int m =board.size();
        int n = board[0].size();
        vector<vector<bool>> dp(m, vector<bool>(n, false));
        for(int i = 0; i < m; i++){
            for (int j = 0; j < n;j++){
                if(search(board, word, dp, 0, i, j)){
                    return true;
                }
            }
        }
        return false;
    }
    bool search(vector<vector<char>>& board, string word, vector<vector<bool>>& dp, int idx, int i, int j){
        if (idx == word.size()){
            return true;
        }
        
        if(i < 0 or j < 0 or i >= board.size() or j >= board[0].size() or word[idx] != board[i][j] or dp[i][j]){
            return false;
        }
        dp[i][j] = true;
        bool res = search(board, word, dp, idx+1, i-1, j) or search(board, word, dp, idx+1, i+1, j) or  search(board, word, dp, idx+1, i, j-1) or  search(board, word, dp, idx+1, i, j+1);
        dp[i][j] = false;
        return res;
    }
};
