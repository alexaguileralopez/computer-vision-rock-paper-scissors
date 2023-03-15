import random
import time
import cv2
from keras.models import load_model
import warnings
warnings.filterwarnings('ignore')
import numpy as np


class RPS():

    def __init__(self):
       # self.timer = int(5)
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.labels = ['Paper', 'Scissors', 'Rock', 'Nothing']
        

    def get_computer_choice(self):
        hand = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(hand)
        
        return computer_choice

    def get_prediction(self):

        text = 'PRESS Q TO START'
        timer = 5
        while True:

            # read and display each frame
            ret, self.frame = self.cap.read()
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(self.frame, str(text), (100, 100), font, 2, (0, 255, 255), 4, cv2.LINE_AA)
            cv2.imshow('Rock Paper Scissors', self.frame)
            
            k = cv2.waitKey(125)

            if k == ord('q'):
                previous_time = time.time()

                while timer >= 0:
                    self.ret, self.frame = self.cap.read()

                    cv2.putText(self.frame, str(timer), (200, 250), font, 7, (0,255,255), 4, cv2.LINE_AA)
                    cv2.imshow('Rock Paper Scissors', self.frame)
                    cv2.waitKey(125)

                    current_time = time.time()

                    # update and keep track if countdown
                    # if time elapsed is one second, decrease the counter by 1

                    if current_time - previous_time >= 1:
                        previous_time = current_time
                        timer = timer - 1

                    # when timer is finished, apply model to frame

                else:
                    ret, self.frame = self.cap.read()
                    resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
                    image_np = np.array(resized_frame)
                    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                    self.data[0] = normalized_image

                    prediction = self.model.predict(self.data, verbose = 0)
                    #print prediction to check it is OK
                    print(prediction)
                    user_choice = self.labels[np.argmax(prediction)]                   

                    #timer = 5
                    
                    return(user_choice)
                              
            elif k == 27:
                break

    def get_winner(self):

        start = time.time()
        computer_wins = 0
        user_wins = 0
        rounds = 0

        while True:

            computer_choice = self.get_computer_choice()
            user_choice = self.get_prediction()

            print("You chose: ", user_choice)

            if computer_choice == 'Paper' and user_choice == 'Rock':
                print('Computer won!')
                computer_wins = computer_wins +1
            elif computer_choice == 'Scissors' and user_choice == 'Paper':
                print('Computer won!')
                computer_wins = computer_wins +1
            elif computer_choice == 'Rock' and user_choice == 'Scissors':
                print('Computer won!')
                computer_wins = computer_wins +1
            elif user_choice == 'Nothing' or None:
                print('Please try again')
            else:
                print('User won!')
                user_wins = user_wins +1
            
            rounds = rounds + 1

            # reaching 5 rounds 
            if rounds == 5 or computer_wins == 3 or user_wins == 3 or user_choice == None:
                break

        if user_wins > computer_wins:
            print("YOU WON THE GAME")
        elif computer_wins > user_wins:
            print("THE COMPUTER WON :(")
        else:
            print('IT IS A TIE!')

        end = time.time()
        print("The time elapsed was", end - start)

        self.cap.release()
        cv2.imshow('Rock Paper Scissors', self.frame)
        cv2.destroyAllWindows()
        cv2.waitKey(1)


game = RPS()
game.get_winner()






            

