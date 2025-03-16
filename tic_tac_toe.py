"""
Tic Tac Toe Game with AI
------------------------
A command-line implementation of the classic Tic Tac Toe game with an unbeatable AI 
using the minimax algorithm. Players can choose to play against another human or AI.

Author: [Wisdom Olaniyan]
Date: [16 of March 2025]
"""

import random
from typing import List, Tuple, Optional
import os
import time

def clear_screen() -> None:
    """Clear the console screen for better UI experience.
    Uses 'cls' for Windows and 'clear' for Unix-based systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board: List[List[str]], message: str = "") -> None:
    """Display the game board and optional message in a formatted way.
    
    Args:
        board: 3x3 list representing the game board
        message: Optional message to display below the board
    """
    clear_screen()
    print("\n=== Tic Tac Toe ===\n")
    print("     0   1   2")
    print("   +---+---+---+")
    for i, row in enumerate(board):
        print(f" {i} | {' | '.join(cell if cell != ' ' else ' ' for cell in row)} |")
        print("   +---+---+---+")
    if message:
        print(f"\n{message}")

def check_winner(board: List[List[str]], player: str) -> bool:
    """Determine if the specified player has won the game.
    
    Args:
        board: Current game board state
        player: Player symbol ('X' or 'O')
    
    Returns:
        bool: True if player has won, False otherwise
    """
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board: List[List[str]]) -> bool:
    """Check if the game board is completely filled.
    
    Args:
        board: Current game board state
    
    Returns:
        bool: True if no empty spaces remain, False otherwise
    """
    return all(cell != " " for row in board for cell in row)

def get_valid_moves(board: List[List[str]]) -> List[Tuple[int, int]]:
    """Get all available valid moves on the board.
    
    Args:
        board: Current game board state
    
    Returns:
        List of tuples containing (row, col) coordinates of empty cells
    """
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board: List[List[str]], depth: int, is_maximizing: bool, ai_player: str) -> int:
    """Implementation of the minimax algorithm for optimal AI moves.
    
    Args:
        board: Current game board state
        depth: Current depth in the game tree
        is_maximizing: Boolean indicating if maximizing or minimizing player
        ai_player: AI's symbol ('X' or 'O')
    
    Returns:
        int: Score of the board position (-1 for loss, 0 for draw, 1 for win)
    """
    human_player = "X" if ai_player == "O" else "O"
    
    if check_winner(board, ai_player):
        return 1
    if check_winner(board, human_player):
        return -1
    if is_full(board):
        return 0
        
    if is_maximizing:
        best_score = float('-inf')
        for i, j in get_valid_moves(board):
            board[i][j] = ai_player
            score = minimax(board, depth + 1, False, ai_player)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_valid_moves(board):
            board[i][j] = human_player
            score = minimax(board, depth + 1, True, ai_player)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def get_ai_move(board: List[List[str]], ai_player: str) -> Tuple[int, int]:
    """Calculate the best possible move for the AI using minimax algorithm.
    
    Args:
        board: Current game board state
        ai_player: AI's symbol ('X' or 'O')
    
    Returns:
        Tuple of (row, col) representing the AI's chosen move
    """
    print_board(board, "AI is thinking...")
    time.sleep(0.5)  # Add a small delay to make AI moves visible
    
    best_score = float('-inf')
    best_move = None
    
    for i, j in get_valid_moves(board):
        board[i][j] = ai_player
        score = minimax(board, 0, False, ai_player)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    
    return best_move or random.choice(get_valid_moves(board))

def get_player_move(board: List[List[str]], player: str) -> Tuple[int, int]:
    """Get and validate human player's move input.
    
    Args:
        board: Current game board state
        player: Current player's symbol ('X' or 'O')
    
    Returns:
        Tuple of (row, col) representing the player's validated move
    """
    while True:
        try:
            print_board(board, f"{player}'s turn. Enter row and column (0-2, space-separated): ")
            row, col = map(int, input().strip().split())
            
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print_board(board, "Numbers must be between 0 and 2!")
                time.sleep(1)
                continue
                
            if board[row][col] != " ":
                print_board(board, "Cell already taken, try again.")
                time.sleep(1)
                continue
                
            return row, col
            
        except (ValueError, IndexError):
            print_board(board, "Invalid input! Please enter two numbers between 0-2 separated by a space.")
            time.sleep(1)

def play_game() -> None:
    """Main game loop handling the game flow and player turns."""
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        turn = 0
        
        clear_screen()
        print("\n=== Tic Tac Toe ===\n")
        game_mode = input("Do you want to play against AI? (yes/no): ").strip().lower()
        while game_mode not in ["yes", "no"]:
            clear_screen()
            print("\n=== Tic Tac Toe ===\n")
            print("Please enter 'yes' or 'no'")
            game_mode = input("Do you want to play against AI? (yes/no): ").strip().lower()
            
        ai_player = "O" if game_mode == "yes" else None
        
        while True:
            player = players[turn % 2]
            
            if player == ai_player:
                row, col = get_ai_move(board, ai_player)
                print_board(board, f"AI plays: {row} {col}")
                time.sleep(1)
            else:
                row, col = get_player_move(board, player)
            
            board[row][col] = player
            
            if check_winner(board, player):
                print_board(board, f"\n{player} wins!")
                time.sleep(1)
                break
            if is_full(board):
                print_board(board, "\nIt's a tie!")
                time.sleep(1)
                break
            
            turn += 1
        
        print("\nPlay again? (yes/no): ")
        play_again = input().strip().lower()
        if play_again != "yes":
            clear_screen()
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()
