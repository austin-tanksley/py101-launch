import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

prompt(f'Choose one: {', '.join(VALID_CHOICES) }')
choice = input().lower()

while choice not in VALID_CHOICES:
    prompt('That is not a valid choice. Try again')
    choice = input().lower()

computer_choice = random.choice(VALID_CHOICES)

prompt(f'You chose {choice}. The computer chose {computer_choice}')

if ((choice == 'rock' and computer_choice == 'scissors') or
    (choice == 'paper' and computer_choice == 'rock') or
    (choice == 'scissors' and computer_choice == 'paper')):
    prompt('You win!')
elif (choice == computer_choice):
    prompt("It's a tie!")
else:
    prompt('Computer wins! :(')
