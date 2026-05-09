from ui import TicTacToeUI

# choose what char for each player
# play AI mode
# score tracker (Player 1 has 3 wins etc)
# animate the expiring cell, flash it before it disappears using window.after()
# sound effects using pygame.mixer or winsound
# real time multiplayer

def main():
    app = TicTacToeUI()
    app.run()    
        
if __name__ == "__main__":
    main()