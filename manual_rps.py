import random

def get_computer_choice():
    hand = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(hand)
    
    return computer_choice



def get_user_choice():
    user_choice = input('Please select your choice in Rock, Paper, Scissors')

    return user_choice


def get_winner(computer_choice, user_choice):

    if computer_choice == 'Paper' and user_choice == 'Rock':
        print("You lost")
    elif computer_choice == 'Scissors' and user_choice == 'Paper' :
        print("You lost")
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        print("You lost")
    elif computer_choice == user_choice:
        print("It is a tie!")
    else:
        print("You won!")

    return

def play():

    get_winner(get_computer_choice(),get_user_choice())

    return

play()


