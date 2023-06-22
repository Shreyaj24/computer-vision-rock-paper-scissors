import random
rps_input = ['Rock', 'Paper', 'Scissors']
def get_computer_choice():
    computer_choice = random.choice(rps_input)
    #print(computer_choice)
    return computer_choice 

def get_user_choice():
    user_choice = input('Please provide your choice:')
    return user_choice


def get_winner (computer_choice , user_choice):
    if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
        print('Computer won')
    elif (computer_choice == 'Rock' and user_choice =='Rock') or (computer_choice == 'Paper' and user_choice == 'Paper') or (computer_choice == 'Scissors' and user_choice == 'Scissors'):
        print("It is a Tie")
    else:
        print('You won')
    

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    game_winner = get_winner(computer_choice,user_choice)
    return game_winner

play()


    
    

    
    
    


    
