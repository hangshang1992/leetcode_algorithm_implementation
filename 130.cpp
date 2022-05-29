class Solution {
public:
    void solve(vector<vector<char>>& board) {
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                if ((i == 0 or i == board.size() - 1 or j == 0 or j == board[0].size() - 1) and board[i][j] == 'O'){
                    dfs(board, i, j);
                }
            }
        }
        for (int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                if (board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                if(board[i][j] == '$'){
                    board[i][j] = 'O';
                }
            }
        }
    }
    void dfs(vector<vector<char>>& board, int i, int j){
        if(board[i][j] == 'O'){
            board[i][j] = '$';
            if (i-1>=0 and board[i-1][j] == 'O'){
                dfs(board, i-1, j);
            }
            if (i +1 < board.size() and board[i+1][j] == 'O'){
                dfs(board, i+1, j);
            }
            if ( j - 1 >= 0 and board[i][j-1] == 'O'){
                dfs(board, i, j -1);
            }
            if (j + 1 < board[i].size() and board[i][j+1] == 'O'){
                dfs(board, i, j+1);
            }
        }
        
    }
};
