# **Computer Vision RPS**
## **Milestone 2**
- **Task 1:**
    -  In this task, craete an image project model with four different classes: Rock, Paper, Scissors and Nothing
- **Task 2:**
    - In this task we download the model from Teachable-Machine.
    - Model named keras_model.h5 and the text file containing the labels should be named labels.txt.
    - Push the files in Github repository.
          
## **Milestone 3**
- **Task 1:**
    - In this task, we create the new virtual environment and install _pip_ to download dependent libraries it depends on. 
    - Create new conda environment, activate and install _pip_ then download opencv-python, tensorflow, and ipykernel using command _pip install_
- **Task 3:**
    - In this task, we create a _requirements.txt_ file by running command _pip list > requirements.txt_.
    - This file enables any other user that wants to use your computer to easily install these exact dependencies by running _pip install requirements.txt_.
- **Task 4:**
    - In this task, we check the downloaded model from _Task 2_ if it is working as expected.

- **Task 5:**
    - In this task, we understand the code given to test the model.

## **Milestone 4**
- **Task 1:**
    -   In this task, we  import random library using _import random_ for random choice by computer to pick a random option between Rock, Paper, and Scissors and then similarly ask user for an input using _input_ function.
    - For above we create two functions:
        - get_computer_choice and get_user_choice.
    - The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.The second function will ask the user for an input and return it.

- **Task 2:**
    - In this task, Python script should choose winner based on the classic rules of Rock-Paper-Scissors.
    for e.g: If the computer chooses rock and the user chooses scissors, the computer wins.
    - Create a function for the above and name it as get_winner by returning the winner.Functions must have two arguments: _computer_choice and user_choice_.
    - If computer wins, it should print "You lost" and vice versa including print "It is a Tie" when both user chooses the same choice.

## **Milestone 5**
- **Task 1:**
    - In this task, we create one function _play_ for all the above functionalities to run the game.
    - Within this function we call the other 3 functions defined above (get_computer_choice, get_user_choice, and get_winner).
     


    



