import cv2
import time
import random
from keras.models import load_model
import numpy as np
computer_wins: int = 0 
user_wins : int = 0
def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    countdown()
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
        user_choice = 'Rock'
    elif highest_prediction == 1:
        print('User chose Paper')
        user_choice = 'Paper'
    elif highest_prediction == 2:
        print('User chose Scissors')
        user_choice = 'Scissors'
    else:
        print('User chose Nothing')  
        user_choice ='Nothing'       
    end_time = time.time()
    print(end_time - start_time)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
                    
        # After the loop release the cap object
    cap.release()
        # Destroy all the windows
    cv2.destroyAllWindows()
    return user_choice 


def countdown():
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



def get_computer_choice():
    rps_input = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(rps_input)
    print(computer_choice)
    return computer_choice 

def get_user_choice():
    user_choice = get_prediction()
    print ("User Choice ", user_choice)
    return user_choice

def get_winner (computer_choice , user_choice):
    global computer_wins 
    global user_wins
    if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
        print('Computer win score before: ', computer_wins)
        computer_wins += 1
        print ('computer won and computer_score: ', computer_wins)
    elif (computer_choice == 'Rock' and user_choice =='Rock') or (computer_choice == 'Paper' and user_choice == 'Paper') or (computer_choice == 'Scissors' and user_choice == 'Scissors'):
        print("It is a Tie")
    else:
        print('User win score before: ', user_wins)
        user_wins += 1
        print ('user won and user_score: ', user_wins)

def play():
    while computer_wins < 3 and user_wins < 3:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        get_winner(computer_choice,user_choice)
    if computer_wins == 3:
         print('computer wins')
    else:
         print('User wins')     
         

play()


