#!/usr/bin/env python3
# Tic Tac Toe game

import random
import sys
import copy

class Game:
    def __init__(self):
        self.board = [' '] * 9
        self.player_name = ''
        self.player_marker = ''
        self.bot_name = 'TBot'
        self.bot_marker = ''
        self.winning_combos = (
            [6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        )
        self.corners = [0, 2, 6, 8]
        self.sides = [1, 3, 5, 7]
        self.middle = 4

    def print_board(self):
        board_display = self.board[:]
        print(f'''
            | {board_display[6]} | {board_display[7]} | {board_display[8]} |
            -------------
            | {board_display[3]} | {board_display[4]} | {board_display[5]} |
            -------------
            | {board_display[0]} | {board_display[1]} | {board_display[2]} |
        ''')

    def get_marker(self):
        marker = input("İşaretin X mi yoksa O mu olsun? (X/O): ").upper() 
        while marker not in ["X", "O"]:
            marker = input("Hatalı giriş! X veya O seçmelisin: ").upper()
        return ('X', 'O') if marker == "X" else ('O', 'X')

    def is_winner(self, board, marker):
        for combo in self.winning_combos:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == marker:
                return True
        return False

    def get_bot_move(self):
        # Kazanma hamlesi ara
        for i in range(9):
            board_copy = copy.deepcopy(self.board)
            if self.is_space_free(board_copy, i):
                board_copy[i] = self.bot_marker
                if self.is_winner(board_copy, self.bot_marker):
                    return i
        
        # Engelleme hamlesi ara
        for i in range(9):
            board_copy = copy.deepcopy(self.board)
            if self.is_space_free(board_copy, i):
                board_copy[i] = self.player_marker
                if self.is_winner(board_copy, self.player_marker):
                    return i

        # Köşe veya merkez tercih et
        for move in [self.middle] + self.corners + self.sides:
            if self.is_space_free(self.board, move):
                return move
        return None

    def is_space_free(self, board, index):
        return board[index] == ' '

    def is_board_full(self):
        return ' ' not in self.board

    def start_game(self):
        print("\n--- Tic-Tac-Toe Oyununa Hoş Geldiniz ---")
        self.player_name = input("Adın nedir? ")
        self.player_marker, self.bot_marker = self.get_marker()
        
        turn = 'h' if random.randint(0, 1) == 1 else 'b'
        print(f"{'Sen' if turn == 'h' else self.bot_name} ilk başlıyor!")
        
        self.enter_game_loop(turn)

    def enter_game_loop(self, turn):
        while True:
            self.print_board()
            if turn == 'h':
                move = int(input("Hamleni yap (1-9): ")) - 1
                if self.is_space_free(self.board, move):
                    self.board[move] = self.player_marker
                    if self.is_winner(self.board, self.player_marker):
                        print("Tebrikler, kazandın!")
                        break
                    turn = 'b'
                else:
                    print("O alan dolu!")
            else:
                move = self.get_bot_move()
                self.board[move] = self.bot_marker
                if self.is_winner(self.board, self.bot_marker):
                    print(f"{self.bot_name} kazandı!")
                    break
                turn = 'h'
            
            if self.is_board_full():
                print("Oyun berabere!")
                break
        self.print_board()

if __name__ == "__main__":
    game = Game()
    game.start_game()
