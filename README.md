# Computer Vision RPS

# Milestone 2

In this milestone, the computer vision system that detects wether the user is showing Rock, Paper or Scissors to the laptop camera.
This is done by going to "Teachable Machine", a website that provides computer vision models. Here, we take several pictures showing Rock, Paper or Scissors, or nothing, to stablish the 4 scenarios that could happen.

The model for this exercise, shows the probability of the user showing "Rock", "Paper", "Scissors", or nothing to the camera. Therefore, everytime that the user plays the game, the model will try to recognise the hand that the user is playing, and display the probability of the four options mentioned before. 


# Milestone 4

In this milestone, the 'Rock, Paper, Scissors' game was created manually. This was done in the file called "manual_rps.py".
First, two functions called "get_computer_choice" and "get_user_choice" were created.

"get_computer_choice" was used to get a random choice between the 3 options given. This was done importing random, to make use of the random function to sellect one of the options in the list that stored the 3 strings. That function returns the random choice the computer made.

"get_user_choice" was used for the user to input one of the 3 choices by typing it, the function accepts that as an input, and it returns it. 

After those two functions were created, a function called "get_winner" was used to merge the use of the previous ones. This new function takes two arguments: "computer_choice" and "user_choice" and compares them. 
Making use of if-elif-else statements, the function compares the computer and user choice, and displays the messages "You won!", "You lost", or "It is a tie!" if the choices are the same. 

Finally, a function called play, which takes no arguments is created. Within that function, the three previous functions are used. Inside "play", the function "get_winner" is called, and the arguments it takes, are the other two functions.
Therefore, the syntax looks like this:

get_winner(get_computer_choice(),get_user_choice())

Hence, this last function, calls "get_winner", which calls "get_computer_choice" and "get_user_choice".


# Milestone 5
In this last milestone, the game was taken to a next step, and the camera was used to replace the choice of the user, and the computer's choice was mantained as earlier. 
In this exercise, several libraries are imported in order to make use of the model, camera and others. 
The model is imported from a downloaded file where computer vision model was created by classifying different photographs of the user showing 'rock', 'paper', 'scissors' and nothing to the camera. The model receives the input from the camera and returns the values of the probabilities that the image pertains to each of the 4 classes. 

The final approach was to use OOP to create the game instance. 
A class called RPS (Roc Paper Scissors) is defined with various attributes such as the model, the videocamera, data and labels.
The first method defined is the "get_computer_choice", which is the same function used in previous milestones. 
However, the method get_prediction, makes use of the camera to get the image from the user and applying the model. 
Text is displayed when the camera is switched on "PRESS Q TO START". 

![Image text] /Users/alexaguilera/Desktop/AiCore/computer-vision-rock-paper-scissors/RPS_Countdown.jpg

When the user presses the key 'q', the countdown from 5 is displayed, and the image is captured, normalized, and inputted to the model, which makes the prediction. Finally, the method returns the user_choice, which is defined by getting the array of predictions, and applying self.labels[np.argmax(prediction)], which only highlights the value in 'labels' that is the highest, therefore, assigns the right label to the user choice. 

The method get_winner makes use of the previously mentioned methods, and defines the winner by adding points to the computer or the user according to the rules of the game. 
Finally, when either computer or user have reached 3 victories, or the game has arrived to 5 rounds, the method stops counting points, and compares the score to give a final winner.

Also, the time elapsed is measured in this last method. 
