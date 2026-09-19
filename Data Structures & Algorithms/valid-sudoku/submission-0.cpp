class Solution {
   public:
    // naive way
    bool checkRow(vector<vector<char>>& board, const int& n, const int& r, const int& c) {
        int value = board[r][c];
        for (int i = 0; i < n; i++) {
            if (i != c && board[r][i] == value) {
                return false;
            }
        }
        return true;
    }
    bool checkColumn(vector<vector<char>>& board, const int& n, const int& r, const int& c) {
        int value = board[r][c];
        for (int i = 0; i < n; i++) {
            if (i != r && board[i][c] == value) {
                return false;
            }
        }
        return true;
    }
    // bool checkGrid(vector<vector<char>>& board, const int& n, const int& r, const int& c) {}

    // or?

    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();
        vector<set<int>> col(n);
        vector<set<int>> row(n);
        vector<set<int>> grid(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int which = 3*(i/3)+j/3;
                // cout << which << ' ';
                if(board[i][j] == '.')continue;
                int value  = board[i][j];
                if(row[i].contains(value)) return false;
                row[i].insert(value);
                if(col[j].contains(value)) return false;
                col[j].insert(value);
                if(grid[which].contains(value)) return false;
                grid[which].insert(value);
            }
        }
        return true;
    }
};
