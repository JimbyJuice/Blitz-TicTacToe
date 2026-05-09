import tkinter as tk
from game import TicTacToeGame, playerToMove, PLAYER1, PLAYER2, UNSET

class TicTacToeUI:
    def __init__(self):
        self.game = TicTacToeGame()
        
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)
        self.window.config(bg="#0f0f1a")
        
        self.statusLabel = tk.Label(self.window, text="Player 1's turn (O)", font=("Arial", 14), bg="#0f0f1a", fg="#ffffff")
        self.statusLabel.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        
        resetBtn = tk.Button(
            self.window, text="RESTART", font=("Courier", 14, "bold"),
            bg="#0f0f1a", fg="#1b400e", activebackground="#1a1a2e",
            relief="flat", bd=0, command=self._reset
        )
        resetBtn.grid(row=4, column=0, columnspan=3, pady=10)
        
        self.warnedCell = None
        
    def create_board(self):
        for row in range(3):
            for col in range(3):
                cell = tk.Frame(self.window, width=120, height=120, bg="#1a1a2e")
                cell.grid(row=row+1, column=col, padx=4, pady=4)
                cell.grid_propagate(False)
                
                btn = tk.Button(
                    cell, text=UNSET, 
                    font=("Courier", 56, "bold"), bg="#1a1a2e", fg="#ffffff",
                    activebackground="#2a2a4e", relief="raised", bd=4,
                    command=lambda r=row, c=col: self._on_click(r, c)
                )
                btn.grid(row=0, column=0, sticky="nsew")
                cell.grid_rowconfigure(0, weight=1)
                cell.grid_columnconfigure(0, weight=1)
                
                self.buttons[row][col] = btn
                
    def _style_button(self, row, col):
        symbol = self.game.get_symbol(row, col)
        btn = self.buttons[row][col]
        if symbol == "O":
            btn.config(text="O", fg="#89CFF0", bg="#1a1a2e", activebackground="#2a2a4e", highlightbackground="#1a1a2e", highlightthickness=0)
        elif symbol == "X":
            btn.config(text="X", fg="#ff2d78", bg="#1a1a2e", activebackground="#2a2a4e", highlightbackground="#1a1a2e", highlightthickness=0)
        else:
            btn.config(text=UNSET, fg="#ffffff", bg="#1a1a2e", activebackground="#2a2a4e", highlightbackground="#1a1a2e", highlightthickness=0)
    
    def _highlight_win(self):
        winningCells = self.game.get_winner_cells()
        for r, c in winningCells:
            self.buttons[r][c].config(bg="#39ff14",activebackground="#39ff14", highlightbackground="#39ff14" )
    
    def _on_click(self, row, col):
        if not self.game.make_move(row, col):
            return
        
        if self.warnedCell is not None:
            r, c = self.warnedCell
            self._style_button(r, c)
            self.warnedCell = None

        if self.game.expiredCell is not None:
            r, c = self.game.expiredCell
            self.buttons[r][c].config(text=UNSET, bg="#1a1a2e", fg="#ffffff")
            
        self._style_button(row, col)
        
        if len(self.game.queue) == 5:
            r, c = self.game.queue[0]
            print(f"clearing warned cell ({r},{c}), current bg: {self.buttons[r][c].cget('bg')}")
            self.buttons[r][c].config(bg="#ffcc00", activebackground="#ffcc00", highlightbackground="#ffcc00")
            self.warnedCell =  (r, c)
        
            
        winner = self.game.check_winner()
        if winner is not None:
            # clear warning cells
            if self.warnedCell is not None:
                r, c = self.warnedCell
                self._style_button(r,c)
                self.warnedCell = None
                
            self._highlight_win()
            winnerNum = 1 if winner == PLAYER1 else 2
            self.statusLabel.config(text=f"*** Player {winnerNum} is the winner! ***")
            for row in self.buttons:
                for btn in row:
                    btn.config(command=lambda: None)
        else:
            current = self.game.currentPlayer
            currentNum = 1 if current == PLAYER1 else 2
            self.statusLabel.config(text=f"Player {currentNum}'s turn ({playerToMove[current]})")
    
    def run(self):
        self.window.mainloop()
        
    def _reset(self):
        self.game._reset()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(
                    text=UNSET, bg="#1a1a2e", 
                    fg="#ffffff",  activebackground="#2a2a4e", 
                    highlightbackground="#1a1a2e", highlightthickness=0,
                    command=lambda r=row, c=col: self._on_click(r, c)
                )
        self.statusLabel.config(text="Player 1's turn (O)", fg="#ffffff")