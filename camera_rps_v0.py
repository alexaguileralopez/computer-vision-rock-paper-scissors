import random
import time
import cv2
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
computer_wins = 0
user_wins = 0

#starting the time
start = time.time()

# this function returns the prediction of the model, 
# by taking the argmax of the array that the model returns
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

# this function returns a random choice between R, P, S
def get_computer_choice():
    hand = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(hand)
    
    return computer_choice

# this function defines who is the winner, 
# by comparing the computer choice and the user choice
def get_winner(computer_choice, user_choice):

    winner = ''

    if computer_choice == 'Paper' and user_choice == 'Rock':
        print("You lost")
        winner = 'Computer'
    elif computer_choice == 'Scissors' and user_choice == 'Paper' :
        print("You lost")
        winner = 'Computer'
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        print("You lost")
        winner = 'Computer'
    elif computer_choice == user_choice:
        print("It is a tie!")
        winner = 'No winner'
    else:
        print("You won!")
        winner = 'User'

    return winner


# this loop uses the Open-CV library to capture the image, and
# it normalizes it. It stores that image as the variable data, which is passed to the model
# model.predict(data)
while True: 
    start = time.time()

    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    user_choice = get_prediction(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("You chose", user_choice)
        end = time.time()
        break
        
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

    



print("The time elapsed is", end-start)
computer_choice = get_computer_choice()
get_winner(computer_choice,user_choice)


    
      



        
    


    













