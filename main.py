'''
Rock, Paper, Scissors game
'''
import random
import sys

class RockPaperScissors:
    def __init__(self):
        print('Welcome to Rock, paper, Scissors!')
        self.moves: dict = {'rock': '🏔️', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list(str) = list(self.moves.keys())

    def play_game(self):
        '''
        Take user choice and check if is valid
        '''
        print('Make your choice or type \'exit\' to end the game')
        user_move: str = input(
            '1 -> Rock 🏔️,\n2 -> Paper 📜 \n3 -> Scissors ✂️  \n>> ').lower()

        match(user_move):
            case '1':
                user_move = 'rock'
            case '2':
                user_move = 'paper'
            case '3':
                user_move = 'scissors'

        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid choice...')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        '''
        Displays user and AI moves
        '''
        print('----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')

    def check_move(self, user_move: str, ai_move: str):
        '''
        Check the player move agains AI move and displays the result
        '''
        if user_move == ai_move:
            print('It\'s a tie!')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
        else:
            print('You lost!')
        print('-----------------------------------')


if __name__ == '__main__':
    rock_paper_scissors = RockPaperScissors()
    while True:
        rock_paper_scissors.play_game()
