import random
import time
import cv2
from keras.models import load_model
import numpy as np

# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
timer = int(5)
text = 'Press Q to start countdown'
   
model = load_model('keras_model.h5')

cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# defining the variables used to count 
# victories and rounds
rounds_played = 0
computer_wins = 0
user_wins=0



# function to assign rock, paper, scissors, to the model output in numbers
def get_prediction(prediction):
    choice = ''
    max = np.argmax(prediction)
    if max == 0:
        choice = 'Paper'
    elif max == 1:
        choice = 'Scissors'
    elif max == 2:
        choice = 'Rock'
    elif max == 3:
        choice = 'Nothing'

    return choice

# function to get a random choice between rock, paper, scissors, 
# which is assigned to the computer choice
def get_computer_choice():
    hand = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(hand)
    
    return computer_choice

# function to define who is the winner
# the fxn returns 1 when computer wins
# returns 0 when user wins 
# returns 2 when it is a tie

def get_winner(computer_choice, user_choice):

    
    if computer_choice == 'Paper' and user_choice == 'Rock':
        return 1
    elif computer_choice == 'Scissors' and user_choice == 'Paper' :
        return 1
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        return 1
    elif computer_choice == user_choice:
        return 2
    else:
        return 0

# function that defines the winner by comparing the variables computer_wins and user_wins    

def define_winner(computer_wins, user_wins):
    if computer_wins > user_wins:
        return "Computer!"
    elif computer_wins < user_wins:
        return "User!"


start = time.time()

# loop that is mantained while 5 rounds have been played or computer or user have won (3 victories)    
while rounds_played < 5 or computer_wins or user_wins < 3:

    # Read and display each frame
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, str(text), 
            (100, 100), font,
            2, (0, 255, 255),
            4, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    
    
    # check for the key pressed
    k = cv2.waitKey(125)
        
    # set the key for the countdown
    # to begin. Here we set q
    # if key pressed is q
    if k == ord('q'):
        prev = time.time()

        while timer >= 0:
            ret, frame = cap.read()

            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, str(timer), 
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)
            cv2.imshow('frame', frame)
            cv2.waitKey(125)

            # current time
            cur = time.time()

            # Update and keep track of Countdown
            # if time elapsed is one second 
            # then decrease the counter
            if cur-prev >= 1:
                prev = cur
                timer = timer-1
        
        # when countdown is finished, apply the model to the frame
        else:
            ret, frame = cap.read()

            # apply the model to that frame that we captured

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            cv2.waitKey(2000)


            user_choice = get_prediction(prediction)
            print("You chose", user_choice)

            computer_choice = get_computer_choice()
            get_winner(computer_choice,user_choice)

            if get_winner(computer_choice,user_choice)== 1:
                computer_wins = computer_wins +1
                print ("You lost!")
            elif get_winner(computer_choice,user_choice)== 0:
                user_wins = user_wins +1
                print("You won!")
            else:
                print("It is a tie!")

            print("Computer wins: ", computer_wins, "\nUser wins: ", user_wins)

            # the rounds played adds 1, and 
            # the timer is reseted
            rounds_played = rounds_played +1
            timer = int(5)

    # Press Esc to exit or play 5 rounds
    elif k == 27 or rounds_played ==5:
        break
    

# close the camera
cap.release()

# close all the opened windows
cv2.destroyAllWindows()

end = time.time()

if computer_wins != user_wins:
    print("GAME OVER, the winner is the ", define_winner(computer_wins, user_wins))
elif computer_wins == user_wins:
    print("GAME OVER, IT IS A TIE!")

print("The time elapsed was", end-start)



