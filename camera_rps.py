import random
import time
import cv2
from keras.models import load_model
import numpy as np

# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
timer = int(5)
   
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)



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

def get_winner(computer_choice, user_choice):

    global computer_wins
    computer_wins = 0
    global user_wins
    user_wins = 0

    if computer_choice == 'Paper' and user_choice == 'Rock':
        print("You lost")
        computer_wins = computer_wins + 1
    elif computer_choice == 'Scissors' and user_choice == 'Paper' :
        print("You lost")
        computer_wins = computer_wins + 1
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        print("You lost")
        computer_wins = computer_wins + 1
    elif computer_choice == user_choice:
        print("It is a tie!")
        
    else:
        print("You won!")
        user_wins = user_wins + 1

    return computer_wins, user_wins


start = time.time()

while True:
      
    # Read and display each frame
    ret, frame = cap.read()
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
            # HERE we can reset the Countdown timer
            # if we want more Capture without closing
            # the camera

            user_choice = get_prediction(prediction)
            print("You chose", user_choice)
  
    # Press Esc to exit
    elif k == 27:
        break
  
# close the camera
cap.release()
   
# close all the opened windows
cv2.destroyAllWindows()

end = time.time()


print("The time elapsed is", end-start)

computer_choice = get_computer_choice()
get_winner(computer_choice,user_choice)

#redefine computer wins and user wins from local to global variables


print("Computer wins: ", computer_wins, "\nUser wins: ", user_wins)


