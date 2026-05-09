import sys
from collections import deque

KNOT = "O"
CROSS = "X"
PLAYER1 = 1
PLAYER2 = -1
UNSET = ' '

playerToMove = {PLAYER1: KNOT, PLAYER2: CROSS}
moveToPlayer = {KNOT: PLAYER1, CROSS: PLAYER2}

# hot seat feature, show which cells are expiring
# choose what char for each player
# quit game button
# play AI mode
# real time multiplayer

def get_player_action(board: list[list[chr]]) -> tuple:
    while True:
        try:
            choice = tuple(map(int, input("\nEnter row col: ").split()))
            
        except ValueError:
            print("Please enter valid input!")
            continue

        except KeyboardInterrupt:
            print("\nSad to see you go :(")
            sys.exit(0)
            
        except EOFError:
            print("\nSad to see you go :(")
            sys.exit(0)
            
        if len(choice) != 2:
            print("Please enter as row col")
            continue
        
        row = choice[0]
        col = choice[1]
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Out of bounds!")
            continue
        
        if board[row][col] == KNOT or board[row][col] == CROSS:
            print("Choice is occupied!")
            continue
        
        return choice

def print_board(board: list[list[chr]]):
    for i in range(len(board)):
        print(' ' + " | ".join(board[i]) + ' ')
        if i < 2:
            print("---+---+---")

def update_board(move, board, currPlayer):
    board[move[0]][move[1]] = playerToMove[currPlayer]
    return board

def checkVertical(board: list[list[chr]], playerSymbol: str):
    if board[0][0] == playerSymbol and board[1][0] == playerSymbol and board[2][0] == playerSymbol:
        return True
    if board[0][2] == playerSymbol and board[1][2] == playerSymbol and board[2][2] == playerSymbol:
        return True
    return None

def checkDiagonal(board: list[list[chr]], playerSymbol: str):
    if board[0][0] == playerSymbol and board[1][1] == playerSymbol and board[2][2] == playerSymbol:
        return True
    if board[0][2] == playerSymbol and board[1][1] == playerSymbol and board[2][0] == playerSymbol:
        return True
    return None
    
def game_finished(board: list[list[chr]]):
    # check horizontal
    for row in board:
        if len(set(row)) == 1 and UNSET not in row:
            # row is all x or o
            return moveToPlayer[row[0]]
    
    if checkVertical(board, playerToMove[PLAYER1]) is not None:
        return PLAYER1
    elif checkVertical(board, playerToMove[PLAYER2]) is not None:
        return PLAYER2
    
    # check diagonal
    if checkDiagonal(board, playerToMove[PLAYER1]) is not None:
        return PLAYER1
    elif checkDiagonal(board, playerToMove[PLAYER2]) is not None:
        return PLAYER2
    
    return None
    

def main():
    board = [
        [UNSET, UNSET, UNSET],
        [UNSET, UNSET, UNSET],
        [UNSET, UNSET, UNSET]
    ]
    currPlayer = PLAYER1
    queue = deque()
    
    print_board(board)
    while (game_finished(board) is None):
        move = get_player_action(board)
        queue.append(move)
        if len(queue) == 6:
            expiredMove = queue.popleft()
            board[expiredMove[0]][expiredMove[1]] = UNSET
        update_board(move, board, currPlayer)
        print_board(board)
        # switch player
        currPlayer = -currPlayer
    
    winner = game_finished(board)
    if winner == PLAYER1:
        winner = "Player 1"
    else:
        winner = "Player 2"
    
    print(f"\n*** {winner} is the winner! ***")


if __name__ == "__main__":
    main()