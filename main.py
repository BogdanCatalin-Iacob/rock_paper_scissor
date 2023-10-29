'''
Rock, Paper, Scissors game
'''
import sys

class RockPaperScissors:
    def __init__(self):
        print('Welcome to Rock, paper, Scissors!')
        self.moves: dict = {'rock': '🏔️', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list(str) = list(self.moves.keys()).append(['1', '2', '3'])

    def play_game(self):
        '''
        Take user choice and check if is valid
        '''
        print('Make your choice or type \'exit\' to end the game')
        user_move: str = input(
            '1 -> Rock 🏔️, 2 -> Paper 📜 or 3 -> Scissors ✂️ >> ').lower()

        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid choice...')
            return self.play_game()

    def display_moves(self):
        ...

    def check_move(self):
        ...
