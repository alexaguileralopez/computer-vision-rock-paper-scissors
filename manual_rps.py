import random

def get_computer_choice():
    hand = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(hand)
    
    return computer_choice



def get_user_choice():
    user_choice = input('Please select your choice in Rock, Paper, Scissors')

    return user_choice

get_computer_choice()