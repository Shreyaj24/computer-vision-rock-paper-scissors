import cv2
import time
import random
from keras.models import load_model
import numpy as np

#Class definition
class Computervisionrps():
    ''' 
    This class is used to represent game computer vision Rock Paper scissor.
    '''
    #Class constructor
    def __init__(self):
        #attributes
        '''
        The attributes initialised for object to play game RPS.
            rps_input : list : random choice for computer
            computer_wins : int : Number of wins for computer
            user_wins : int : Number of wins for user
        '''
        self.rps_input =  ['Rock', 'Paper', 'Scissors']
        self.computer_wins = 0
        self.user_wins = 0
        
    #methods
    def get_computer_choice(self):
        '''
        This method is for computer to choose random from rps_input
        '''
        self.computer_choice = random.choice(self.rps_input)
        print(self.computer_choice)

    def get_user_choice(self):
        '''
        This method is for user to provide the choice using webcame via get_prediction method.
        '''
        self.get_prediction()
        print ("User Choice ", self.user_choice)
    
    def get_prediction(self):
        '''
        This method predicts the user gesture and provides the data from the image
        '''
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.countdown()
        start_time = time.time()
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        highest_prediction = np.argmax(prediction)
        print(highest_prediction)
        if highest_prediction == 0:
            print('User chose Rock')
            self.user_choice = 'Rock'
        elif highest_prediction == 1:
            print('User chose Paper')
            self.user_choice = 'Paper'
        elif highest_prediction == 2:
            print('User chose Scissors')
            self.user_choice = 'Scissors'
        else:
            print('User chose Nothing')  
            self.user_choice ='Nothing'       
        end_time = time.time()
        print(end_time - start_time)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
                    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        #return self.user_choice 

    def countdown(self):
        '''
        This method provides the countdown for user to be ready to start the game and provide the gesture.
        '''
        t = 0
        i = 0
        j : int = 5
        start_counter = time.time()
        while t <= 6:
            end_counter = time.time()
            t = int(end_counter -start_counter)
            if t in ( 1, 2, 3, 4, 5, 6) and i!=t: 
                print(j)
                j -= 1
            i = t
        print('Start')    

    def get_winner (self):
        '''
        This method provides by checking the input from user and computer for the winner by the rules.
        '''
        if (self.computer_choice == 'Rock' and self.user_choice == 'Scissors') or (self.computer_choice == 'Paper' and self.user_choice == 'Rock') or (self.computer_choice == 'Scissors' and self.user_choice == 'Paper'):
            print('Computer win score before: ', self.computer_wins)
            self.computer_wins += 1
            print ('computer won and computer_score: ', self.computer_wins)
        elif (self.computer_choice == 'Rock' and self.user_choice =='Rock') or (self.computer_choice == 'Paper' and self.user_choice == 'Paper') or (self.computer_choice == 'Scissors' and self.user_choice == 'Scissors'):
            print("It is a Tie")
        else:
            print('User win score before: ', self.user_wins)
            self.user_wins += 1
            print ('user won and user_score: ', self.user_wins)


def play():
    '''
    This function calls the class Computervisionrps to play the game.
    '''
    rps_game = Computervisionrps()
    while rps_game.computer_wins < 3 and rps_game.user_wins < 3:
        rps_game.get_computer_choice()
        rps_game.get_user_choice()
        rps_game.get_winner()
    if rps_game.computer_wins == 3:
         print('computer wins')
    else:
         print('User wins')  

play()                    
                   