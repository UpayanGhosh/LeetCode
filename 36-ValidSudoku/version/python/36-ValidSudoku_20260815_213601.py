# Last updated: 15/08/2026, 21:36:01
# Simply we need to validate each condition once by one. First check the rows if that value is in the rows set then column then the squares. And if present return false else update the sets with the current board values and return True at the end.
1class Solution(object):
2    def isValidSudoku(self, board):
3        cols = collections.defaultdict(set)
4        rows = collections.defaultdict(set)
5        squares = collections.defaultdict(set)
6
7        for r in range(9):
8            for c in range(9):
9                if (board[r][c] == "."):
10                    continue
11                if (board[r][c] in rows[r] or 
12                    board[r][c] in cols[c] or
13                    board[r][c] in squares[(r //3, c//3)]):
14                    return False
15                cols[c].add(board[r][c])
16                rows[r].add(board[r][c])
17                squares[(r //3, c //3)].add(board[r][c])
18        return True
19        