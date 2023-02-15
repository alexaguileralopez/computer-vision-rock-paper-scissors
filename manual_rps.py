import random

def get_computer_choice():
    hand = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(hand)
    
    return computer_choice



def get_user_choice():
    user_choice = input('Please select your choice in Rock, Paper, Scissors')

    while True:
        if user_choice != 'Rock' or 'Paper' or 'Scissors':
            print('Try typing that again')
        else:
            break
    return user_choice


def get_winner():

    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    if user_choice == 'Rock' and computer_choice == 'Paper':
        print("You lost")
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        print("You lost")
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        print("You lost")
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You won!")

    return

    


