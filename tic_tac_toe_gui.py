"""
Tic Tac Toe Game with GUI
-------------------------
A graphical implementation of the Tic Tac Toe game using Tkinter,
featuring an unbeatable AI using the minimax algorithm.

Author: [Wisdom Olaniyan]
Date: [16 of March 2025]
"""

import tkinter as tk
from tkinter import messagebox
import random
from typing import List, Tuple, Optional
import winsound  # Windows only
# Or use pygame.mixer for cross-platform support

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)
        
        # Game variables
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.ai_player = None
        
        # GUI elements
        self.create_menu_frame()
        self.create_game_board()
        self.create_status_label()
        
        # Bindings
        self.window.bind('<Escape>', lambda e: self.window.quit())
        self.window.bind('n', lambda e: self.new_game())
        
    def create_menu_frame(self):
        """Create the game mode selection menu."""
        self.menu_frame = tk.Frame(self.window, pady=10)
        self.menu_frame.pack()
        
        tk.Label(self.menu_frame, text="Play against:").pack(side=tk.LEFT)
        
        self.game_mode = tk.StringVar(value="human")
        tk.Radiobutton(self.menu_frame, text="Human", variable=self.game_mode, 
                      value="human", command=self.new_game).pack(side=tk.LEFT)
        tk.Radiobutton(self.menu_frame, text="AI", variable=self.game_mode,
                      value="ai", command=self.new_game).pack(side=tk.LEFT)
        
        tk.Button(self.menu_frame, text="New Game", 
                 command=self.new_game).pack(side=tk.LEFT, padx=10)

    def create_game_board(self):
        """Create the game board with buttons."""
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.board_frame,
                    text="",
                    font=('Arial', 20, 'bold'),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j].config(
                    bg='lightgray',
                    activebackground='gray',
                    fg='navy'
                )

    def create_status_label(self):
        """Create the status label for game messages."""
        self.status_label = tk.Label(
            self.window,
            text="X's turn",
            font=('Arial', 12),
            pady=10
        )
        self.status_label.pack()

    def new_game(self):
        """Reset the game board and start a new game."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.ai_player = "O" if self.game_mode.get() == "ai" else None
        
        # Reset buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state=tk.NORMAL)
        
        self.status_label.config(text="X's turn")
        
        # If AI goes first
        if self.ai_player == "X":
            self.make_ai_move()

    def make_move(self, row: int, col: int):
        """Handle player moves."""
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner(self.current_player):
                self.end_game(f"{self.current_player} wins!")
                return
            elif self.is_full():
                self.end_game("It's a tie!")
                return
            
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"{self.current_player}'s turn")
            
            # AI's turn
            if self.ai_player == self.current_player:
                self.window.after(500, self.make_ai_move)

    def make_ai_move(self):
        """Make AI move using minimax algorithm."""
        row, col = self.get_ai_move()
        self.make_move(row, col)

    def get_ai_move(self) -> Tuple[int, int]:
        """Calculate the best move for AI."""
        best_score = float('-inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.ai_player
                    score = self.minimax(False)
                    self.board[i][j] = " "
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        return best_move

    def minimax(self, is_maximizing: bool) -> int:
        """Minimax algorithm implementation."""
        human_player = "X" if self.ai_player == "O" else "O"
        
        if self.check_winner(self.ai_player):
            return 1
        if self.check_winner(human_player):
            return -1
        if self.is_full():
            return 0
            
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.ai_player
                        score = self.minimax(False)
                        self.board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = human_player
                        score = self.minimax(True)
                        self.board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, player: str) -> bool:
        """Check if the specified player has won."""
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False

    def is_full(self) -> bool:
        """Check if the board is full."""
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def end_game(self, message: str):
        """Handle game end conditions."""
        self.status_label.config(text=message)
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)
        
        if messagebox.askyesno("Game Over", f"{message}\nPlay again?"):
            self.new_game()

    def highlight_winner(self, winning_cells):
        for row, col in winning_cells:
            self.buttons[row][col].config(bg='lightgreen')

    def play_sound(self, sound_type):
        if sound_type == "move":
            winsound.Beep(440, 50)
        elif sound_type == "win":
            winsound.Beep(880, 200)

    def run(self):
        """Start the game."""
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run() 