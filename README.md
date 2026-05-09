# Blitz Tic Tac Toe 
A Tic Tac Toe desktop game built with Python and tkinter, featuring a hot seat mechanic where moves expire after 3 turns to prevent perpetual draws like in regular Tic Tac Toe.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![tkinter](https://img.shields.io/badge/GUI-tkinter-orange?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows-lightgrey?style=flat-square)

---

## Features

- **Hot Seat Expiry**: each player can only have 3 moves on the board at any time. The oldest move disappears when a 4th is placed, keeping the board dynamic and prevent deadlocks.
- **Expiry Warning**: the cell about to expire is highlighted in yellow so players can plan around it
- **Win Detection**: horizontal, vertical and diagonal wins are all recognised, with the winning three cells highlighted in green
- **Restart**: reset the board at any point without relaunching the app

---

## How to Play

1. Player 1 is **O**, Player 2 is **X**
2. Players alternate clicking cells to place their symbol
3. After each player has placed 3 moves, their oldest move disappears when they place a new one
4. The **yellow cell** is a warning — it will expire on the next move
5. First to get 3 in a row (horizontal, vertical or diagonal) wins

---

## Project Structure

```
TicTacToe/
├── main.py       # Entry point
├── game.py       # Game logic: board state, move validation and win detection
└── ui.py         # tkinter GUI: rendering, styling and user interaction
```

---
## Getting the App
Download the app in the dist folder. Note that this may not be the latest
version. To get use the latest version, please refer to the below.

## Running Locally

**Requirements:** Python 3.10+, tkinter (included in standard Python installs)

```bash
git clone https://github.com/JimbyJuice/tictactoe.git
cd tictactoe
python main.py
```

---

## Building a Standalone Executable

Uses [PyInstaller](https://pyinstaller.org/) to bundle into a single file.

For MacOS:
```bash
pip3 install pyinstaller
pyinstaller --onefile --windowed --icon=icon.icns main.py
```

For Windows (Untested):
```bash
pip3 install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

The executable is output to the `dist/` folder. Share that file directly.

> **Note:** executables are platform-specific. Build on Mac to get a Mac app, build on Windows to get a `.exe`.

---

## Roadmap

- [ ] Score tracker across rounds
- [ ] Choose your own symbol
- [ ] AI opponent (easy, medium and hard)
- [ ] Sound effects
- [ ] Online multiplayer
- [ ] Migration to React.js

---

## Architecture Notes

### `game.py` — TicTacToeGame

### `ui.py` — TicTacToeUI

---

## License

MIT