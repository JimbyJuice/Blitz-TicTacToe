from collections import deque

KNOT = "O"
CROSS = "X"
PLAYER1 = 1
PLAYER2 = -1
UNSET = ' '

playerToMove = {PLAYER1: KNOT, PLAYER2: CROSS}
moveToPlayer = {KNOT: PLAYER1, CROSS: PLAYER2}

def checkVertical(board: list[list[chr]], playerSymbol: str):
    for c in range(3):
        if board[0][c] == playerSymbol and board[1][c] == playerSymbol and board[2][c] == playerSymbol:
            return True
    return None

def checkDiagonal(board: list[list[chr]], playerSymbol: str):
    if board[0][0] == playerSymbol and board[1][1] == playerSymbol and board[2][2] == playerSymbol:
        return True
    if board[0][2] == playerSymbol and board[1][1] == playerSymbol and board[2][0] == playerSymbol:
        return True
    return None
    
class TicTacToeGame:
    def __init__(self):
        self.board = [
            [UNSET, UNSET, UNSET],
            [UNSET, UNSET, UNSET],
            [UNSET, UNSET, UNSET]
        ]
        self.currentPlayer = PLAYER1
        self.queue = deque()
        self.expiredCell = None

    def make_move(self, row, col) -> bool:
        """Attempt a move. Return True if valid or false is cell occupied"""
        if self.board[row][col] != UNSET:
            return False

        self.queue.append((row, col))
        self.expiredCell = None
        
        if len(self.queue) == 6:
            expired = self.queue.popleft()
            self.board[expired[0]][expired[1]] = UNSET
            self.expiredCell = expired
        
        self.board[row][col] = playerToMove[self.currentPlayer]
        self.currentPlayer = -self.currentPlayer
        return True
    
    def check_winner(self):
        # check horizontal
        for row in self.board:
            if len(set(row)) == 1 and UNSET not in row:
                # row is all x or o
                return moveToPlayer[row[0]]
        
        if checkVertical(self.board, playerToMove[PLAYER1]) is not None:
            return PLAYER1
        elif checkVertical(self.board, playerToMove[PLAYER2]) is not None:
            return PLAYER2
        
        # check diagonal
        if checkDiagonal(self.board, playerToMove[PLAYER1]) is not None:
            return PLAYER1
        elif checkDiagonal(self.board, playerToMove[PLAYER2]) is not None:
            return PLAYER2
        
        return None
    
    def get_winner_cells(self):
        # check horizontal
        for r in range(3):
            row = self.board[r]
            if len(set(row)) == 1 and UNSET not in row:
                return [(r, 0), (r, 1), (r, 2)]    
        
        # check columns
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] != UNSET:
                return [(0, c), (1, c), (2, c)]
        
        # check diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != UNSET:
            return [(0, 0), (1, 1), (2, 2)]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != UNSET:
            return [(0, 2), (1, 1), (2, 0)]
        
        return []
    
    def get_symbol(self, row, col) -> str:
        return self.board[row][col]
    
    def _reset(self):
        self.__init__()