import os
from random import choice


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_statistics(scores):
    return f'Wins: {scores["Win"]}\nLosses: {scores["Lose"]}\nDraws: {scores["Draw"]}'


def player_choice():
    while True:
        print('Rock, paper or scissors?')
        choice = input('>').capitalize()
        if choice in ('Rock', 'Paper', 'Scissors'):
            return choice


def computer_choice():
    return choice(('Rock', 'Paper', 'Scissors'))


def game_outcome(player, computer):
    RULES = {
        ('Paper', 'Rock'): 'covers',
        ('Rock', 'Scissors'): 'crushes',
        ('Scissors', 'Paper'): 'cuts'
    }
    if player == computer:
        print('Draw. Nobody wins or losses.')
        return 'Draw'
    elif (player, computer) in RULES:
        print(f'{player} {RULES[player, computer]} {computer}. You won!')
        return 'Win'
    else:
        print(f'{computer} {RULES[computer, player]} {player}. You lost!')
        return 'Lose'


def rock_paper_scissors(scores):
    clear_console()
    print(show_statistics(scores))
    player = player_choice()
    computer = computer_choice()
    outcome = game_outcome(player, computer)
    scores[outcome] += 1
    return scores


def play_again():
    while True:
        print('\nDo you want to play again?')
        print('(Y)es')
        print('(N)o')
        ans = input('> ').lower()
        if ans == 'y':
            return True
        elif ans == 'n':
            return False


def main():
    scores = {
        'Win': 0,
        'Lose': 0,
        'Draw': 0
    }
    still_playing = True
    while still_playing:
        scores = rock_paper_scissors(scores)
        still_playing = play_again()


if __name__ == '__main__':
    main()
