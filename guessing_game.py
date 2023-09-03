import random
from random import randint
# Displays the title and programming specifications

def display_title():
    print(
    '''
    This is a guessing game.
    It will randomly select a number between 1 and 10.
    You will be prompted to enter a guess.
    If your guess is too low, the computer will print "Too low".
    If you guess is too high, the computer will print "Too high".
    If you manage to guess the correct number, the computer will print
    "You guessed it".
    You will be given an option to play another game or exit afterwards.
    ''')


# 
def play_game():
    # Get a random number (1 - 10) that the user has to guess
    random_number = randint(1,10)
    # Variable to store the user's guess
    user_guess = 0


    # While statement to have the user guess
    while True:

        # Input validation - making sure the user enters a number
        try:
            user_guess = int(input('Guess a number between 1 and 10: '))
        except:
            print('Invalid input. You must enter a whole number')

        # the user's guess is too low
        if user_guess < random_number:
            print('Too low')
        # the user's guess is too high
        elif user_guess > random_number:
            print('Too high')
        # otherwise the user guessed the right number
        else:
            print(f'You guess it\nThe correct number was {random_number}')
            # exit out of the play_game function and go back to main()
            return
    
def main():
    # Display the title and information about the game
    display_title()
    # variable that will hold value 'yes'
    continue_game = 'yes'

    # player will keep playing game if the value is yes.
    while continue_game == 'yes':
        # call the play_game function
        print('\n\nStarting the game...')
        play_game()
        
        # input validation - making sure user enters yes or no
        while True:
            continue_game = input('"Yes" to play again. "No" to exit: ').lower()
            if continue_game == 'yes' or continue_game == 'no':
                break
    # The user entered "no" so the program exits.
    print('Goodbye!')

# call the main function to start the game
main()
