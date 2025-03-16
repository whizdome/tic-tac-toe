# Tic Tac Toe with GUI and CLI

A Python implementation of the classic Tic Tac Toe game featuring both GUI and command-line interfaces. The game includes an unbeatable AI opponent using the minimax algorithm.

![Game Screenshot](screenshots/game.png)

## Features

- Two interface options:
  - Graphical User Interface (GUI) using Tkinter
  - Command Line Interface (CLI)
- Two game modes:
  - Player vs Player
  - Player vs AI (unbeatable)
- Smart AI using minimax algorithm
- Clean and intuitive interface
- Cross-platform compatibility

## Requirements

- Python 3.6 or higher
- Tkinter (included in standard Python installation)
- No other external dependencies required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/whizdome/tic-tac-toe.git
cd tic-tac-toe
```

2. Run the GUI version:
```bash
python tic_tac_toe_gui.py
```

Or run the CLI version:
```bash
python tic_tac_toe.py
```

## How to Play

### GUI Version

1. Select game mode using the radio buttons (Human vs Human or Human vs AI)
2. Click "New Game" to start
3. Click on any empty cell to make a move
4. The status label shows current player's turn
5. Game ends when there's a winner or tie
6. Click "Yes" on the popup to play again

### CLI Version

1. Choose game mode (AI or human opponent)
2. Enter moves using row and column numbers (0-2)
3. Follow the on-screen prompts
4. Type "yes" to play again when game ends

## Game Controls

### GUI Version
- Mouse clicks for moves
- 'N' key for new game
- 'Esc' key to quit

### CLI Version
- Enter moves as two numbers separated by space (e.g., "1 1" for center)
- Row and column numbers range from 0 to 2

## Project Structure 