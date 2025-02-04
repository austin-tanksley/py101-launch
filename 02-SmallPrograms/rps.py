import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'rock' and computer ==  'lizard') or
        (player == 'paper' and computer == 'rock') or
        (player == 'paper' and computer == 'spock') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'scissors' and computer == 'lizard') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'lizard' and computer == 'paper') or
        (player == 'spock' and computer == 'rock') or
        (player == 'spock' and computer == 'scissors')):
        prompt('You win!')
    elif player == computer:
        prompt("It's a tie!")
    else:
        prompt('Computer wins! :(')

while True:
    prompt(f'Choose one: {', '.join(VALID_CHOICES) }')
    choice = input().lower()

    while choice not in VALID_CHOICES:
        prompt('That is not a valid choice. Try again')
        choice = input().lower()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}. The computer chose {computer_choice}')

    display_winner(choice, computer_choice)

    prompt('Play again? (y/n)?')
    answer = input().lower()

    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "no".')
        answer = input().lower()

    if answer[0] == 'n':
        break
